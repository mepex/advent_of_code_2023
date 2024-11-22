import re

from Graph import Graph

g = Graph()
g.weighted = True
g.directed = False

f = "input.txt"
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.search("(\w+) to (\w+) = (\d+)", line)
        if m:
            g.add(m.group(1), m.group(2), int(m.group(3)))

all = []
for n in g.nodes:
    d = g.get_hamiltonian_paths(n)
    for p in d:
        w = g.get_path_weight(p)
        all.append(w)
        print(f"{p} weight: {w}")
    print(d)

print(sorted(all)[0])

print(f"part 2: {sorted(all)[-1]}")


