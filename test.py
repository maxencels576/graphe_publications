import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

csvfile = 'graphe_publications/airports.csv'
data = pd.read_csv(csvfile)
data_subset = data.head(1400)
edges = data_subset[['City', 'Country']]
G = nx.Graph()
G.add_edges_from(edges.values)
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, font_size=10, font_weight='bold', node_size=1000)
plt.show()