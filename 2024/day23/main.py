import networkx as nx
from mymodule import *

lines = get_lines('input.txt')
g = nx.Graph()
for l in lines:
    c = l.split('-')
    g.add_edge(c[0], c[1])

triads = set()
with_t = set()
n = g.nodes
for node in n:
    for e in range(len(g.edges(node))-1):
        a = list(g.edges(node))[e][1]
        for v in g.edges(a):
            b = list(v)[1]
            if (node, b) in g.edges:
                l = sorted([node, a, b])
                triads.add(tuple(l))
                if node.startswith('t') or a.startswith('t') or b.startswith('t'):
                    with_t.add(tuple(l))

print(len(triads))
print(triads)
print(len(with_t))
print(with_t)

g2 = nx.make_max_clique_graph(g)

print('part 2:')
for gr in nx.enumerate_all_cliques(g):
  print(','.join(sorted(gr)))
