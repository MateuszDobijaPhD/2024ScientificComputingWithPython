# EXERCISE 12.2
#
# Create a random undirected graph G with more then 5 nodes. Send the script and the figure of the graph.

import networkx as nx
import matplotlib.pyplot as plt

graph = nx.gnp_random_graph(n=12, p=0.5, seed=None, directed=False)
nx.draw(graph)
plt.savefig('figure.png')
plt.show()
