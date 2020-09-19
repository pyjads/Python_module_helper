# %%
import networkx as nx
import matplotlib.pyplot as plt
import nxviz as nz

# %%
# initialize the graph
G = nx.Graph()

# add nodes
G.add_nodes_from([1, 2, 3])

# print the nodes
print(G.nodes())

# %%

# adding data to the node, you have to mention node name here 1 is the node name not the index
G.nodes[1]['label'] = 'blue'

# printing nodes with the data
print(G.nodes(data=True))

# %%

# adding edges unweighted and undirected
G.add_edge(1, 2)
G.edges[(1, 2)]['label'] = 'cutie'
print(G.edges())

# to
print(G.edges(data=True))
# %%
# draw the graph
nx.draw(G)

# you also need matplotlib to show the graph
plt.show()

# %%
# to work with the directed graph use DiGraph
D = nx.DiGraph()
print(type(D))

# you can also initiate multiGraph
M = nx.MultiGraph()

# multiDiGraph
MD = nx.MultiDiGraph()

# %%

# you can use nxviz to for matrix plot or circos plot or arc plot

# https://stackoverflow.com/questions/53366634/how-to-set-edge-color-in-nxviz-arcplot
D = nx.DiGraph()
D.add_nodes_from([1, 2, 3])
D.add_edge(1, 2)
D.add_edge(2, 3)

m = nz.MatrixPlot(D)
m.draw()
plt.show()

a = nz.ArcPlot(D)
a.draw()  # here you can provide node_order and node_color which is provided in nodes metadata
plt.show()

c = nz.CircosPlot(D)
c.draw()
plt.show()
# %%

# to get the neighbours of the node
D = nx.DiGraph()
D.add_nodes_from([1, 2, 3])
D.add_edge(1, 2)
D.add_edge(2, 3)

list(D.neighbors(2))  # this is the directed graph

G = nx.Graph()
G.add_nodes_from([1, 2, 3])
G.add_edge(1, 2)
G.add_edge(2, 3)

print(list(G.neighbors(2)))  # this is the undirected graph

b = nx.barbell_graph(m1=5, m2=2)
nx.draw(b)
plt.show()

# %%
# degree centrality = number of neighbours I have / number of neighbours I could possibly have
# degree centrality tells us about the highly connected node

G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edge(1, 2)
G.add_edge(2, 3)
# G.add_edge(2,2)

print(nx.degree_centrality(G))  # self loops are not considered here and should not be mentioned during edge creation

# %%

# betweeness centrality = number of shortest path through nodes/ all possible shortest paths
# it tells us about the bottleneck path
b = nx.barbell_graph(m1=5, m2=2)
print(nx.betweenness_centrality(b))

# %%
# generating the graph using erdos_renyi_graph

E = nx.erdos_renyi_graph(20, 0.2) # 20 is the number of nodes and 0.2 is the probability that edge should exist between
# nx.connected_component(E) --> it tells us about the how many subgraphs are there in E

print(nx.degree_centrality(E))

# pagerank concept explained below again with directed graph
pr = [nx.pagerank(G)]
import pandas as pd

print(pd.DataFrame(pr))

# two nodes
nx.draw(E)
plt.show()

# %%


E = nx.erdos_renyi_graph(20, 0.2)  # 20 is the number of nodes and 0.2 is the probability that edge should exist between
# two nodes
nodes = list(E.neighbors(1))
nodes.append(1)

# generate the subgraph of graph E with nodes nodes
S = E.subgraph(nodes)
print(S.edges())

nx.draw(S, with_labels=True)
plt.show()
# %%
# pagerank concept
import random

N = 7
G = nx.erdos_renyi_graph(20, 0.2)
for (start, end) in G.edges:
    G.edges[start, end]['weight'] = random.random()
t = nx.pagerank(G)
print(t)
nx.draw(G, with_labels=True)
plt.show()

#%%
# connected component
G = nx.erdos_renyi_graph(20, 0.1)
print(list(nx.find_cliques(G)))
t = sorted(list(nx.connected_components(G)), key=lambda x: len(x))[-1]
print(t)

L = nx.subgraph(G, t)
nx.draw(L)
plt.show()

t = nx.connected_components(G)
i = 1
for n in t:
    for k in n:
        G.nodes[k]['grouping'] = i
        G.nodes[k]['alphabetically'] = i
    i+=1

c = nz.CircosPlot(G, node_grouping='alphabetically', node_color='grouping')
c.draw()
plt.show()

#%%
