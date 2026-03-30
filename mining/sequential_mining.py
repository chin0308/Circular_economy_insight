import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

def load_lifecycle_data(csv_path):
    df = pd.read_csv(csv_path)
    sequences = df.groupby("ProductID")["EventType"].apply(list).tolist()
    return sequences

def mine_frequent_sequences(sequences, min_support=0.5):
    te = TransactionEncoder()
    te_array = te.fit(sequences).transform(sequences)
    df = pd.DataFrame(te_array, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    return frequent_itemsets

def visualize_sequence_graph(sequences):
    G = nx.DiGraph()
    for seq in sequences:
        for i in range(len(seq) - 1):
            src, dst = seq[i], seq[i+1]
            if G.has_edge(src, dst):
                G[src][dst]['weight'] += 1
            else:
                G.add_edge(src, dst, weight=1)
    pos = nx.spring_layout(G)
    weights = [G[u][v]['weight'] for u,v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color=weights, width=2.0, edge_cmap=plt.cm.Blues)
    plt.title("Lifecycle Event Transition Graph")
    plt.show()

def cluster_product_lifecycles(sequences):
    sequence_strs = [' '.join(seq) for seq in sequences]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(sequence_strs)
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)
    for i, label in enumerate(labels):
        print(f"Product {i+1}: Cluster {label}, Events: {sequences[i]}")
