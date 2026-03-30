from mining.sequential_mining import load_lifecycle_data, mine_frequent_sequences, visualize_sequence_graph, cluster_product_lifecycles
from models.pci_calculator import calculate_pci

def main():
    data_path = "data/lifecycle_data.csv"
    sequences = load_lifecycle_data(data_path)

    print("\n🧠 Running PCI Calculation:")
    for i, seq in enumerate(sequences):
        pci = calculate_pci(seq)
        print(f"Product {i+1}: Events = {seq}, PCI = {pci}")

    print("\n🔍 Running Sequential Pattern Mining:")
    results = mine_frequent_sequences(sequences, min_support=0.4)
    print(results)

    print("\n📊 Visualizing Product Lifecycle Graph:")
    visualize_sequence_graph(sequences)

    print("\n🧬 Clustering Lifecycle Patterns:")
    cluster_product_lifecycles(sequences)

if __name__ == "__main__":
    main()
