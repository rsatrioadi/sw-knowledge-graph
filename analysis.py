import networkx as nx

G = nx.read_edgelist(
  'jhotdraw.edgelist',
  create_using=nx.DiGraph,
)

G.number_of_nodes(), G.number_of_edges()

labels = nx.get_edge_attributes(G, 'label')
labels

import re
self_labels = { n1:re.match(r'let:name = string:"(.+)"', label).group(1) \
  for (n1,n2),label in labels.items() \
  if n1==n2 and label.startswith('let:') }
self_labels

nx.draw_kamada_kawai(G, labels=self_labels)
