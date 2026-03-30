**Quantifying Circularity: Circular Economy Insight Engine**

**Overview**

This project presents a data-driven framework to quantify product circularity and analyze lifecycle sustainability. It introduces the Circular Economy Insight Engine, which integrates data warehousing, sequential pattern mining, and interactive visualization to support decision-making in circular economy systems.

The system enables tracking of product lifecycle events and evaluates sustainability using a composite metric called the Product Circularity Index (PCI).

**Objectives**
- Analyze product lifecycle data across multiple stages
- Identify patterns in manufacturing, usage, repair, reuse, recycling, and disposal
- Quantify circularity using PCI
- Provide actionable insights through an interactive dashboard

**Key Features**
- Lifecycle event tracking and analysis
- Sequential pattern mining using PrefixSpan
- Product Circularity Index (PCI) computation
- Interactive dashboard built with Streamlit
- Data visualization for event distribution and lifecycle timelines
- Comparative analysis across product categories

**System Architecture**
The framework integrates:
- Data ingestion from lifecycle datasets
- Data preprocessing and validation
- Sequential mining for pattern discovery
- PCI computation
- Visualization and dashboard interface

<img width="635" height="100" alt="image" src="https://github.com/user-attachments/assets/b2af2659-31ea-480d-b9c9-fb111d686125" />

**Tech Stack**
- Python 3.10
- Pandas
- NumPy
- Matplotlib / Seaborn
- Streamlit

**Dataset**
- Synthetic dataset of 50 products
- 218 lifecycle event sequences
- Events include:
  - Manufacture
  - Usage
  - Repair
  - Reuse
  - Recycling
  - Disposal

**Methodology**
1. Data Collection and Preprocessing : Lifecycle data is stored in CSV format and processed using Pandas.
  
2. Sequential Pattern Mining : PrefixSpan is used to identify frequent lifecycle patterns without candidate generation.
  
3. Circularity Evaluation : PCI is calculated based on reuse, repair, recycling, and disposal factors.
  
4. Visualization : Interactive dashboard displays:
   - Event distribution
   - Lifecycle timelines
   - PCI scores

**Results**
- Average PCI score: 0.55 (moderate circularity)
- High-performing products showed strong reuse and recycling loops
- Linear lifecycle patterns (manufacture → usage → disposal) were still dominant
- Repair and reuse events were underrepresented

Category Insights
- Electronics and plastics showed low circularity
- Furniture and metal products demonstrated higher circularity due to better repair and recycling cycles

Key Insights
- Imbalance in lifecycle stages (low repair and reuse)
- Clear distinction between linear and circular product pathways
- PCI effectively benchmarks sustainability performance

**Installation and Setup**

git clone https://github.com/chin0308/Circular_economy_insight.git

cd Circular_economy_insight

pip install -r requirements.txt

streamlit run app.py

**Future Scope**
- Integration with real-world datasets (IoT, ERP systems)
- Enhanced PCI with weighted parameters
- Inclusion of environmental impact metrics (LCA)
- Real-time lifecycle tracking using digital product passports

**Use Cases**
- Sustainability analysis for manufacturers
- Policy-making and circular economy planning
- Product lifecycle optimization
- Decision support for circular design strategies
