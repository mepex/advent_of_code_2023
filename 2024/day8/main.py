import re
from itertools import combinations
from pprint import pprint
from mymodule import *

grid = []
nodes = {}
f = 'input.txt'
with open(f) as fp:
    i = 0
    for line in fp:
        line = line.strip()
        grid.append(line)
        j = 0
        for ch in line:
            if ch != '.':
                if ch not in nodes:
                    nodes[ch] = []
                nodes[ch].append((i, j))
            j += 1
        i += 1

size = (len(grid), len(grid[0]))
antinodes = []
for n in nodes.keys():
    spots = nodes[n]
    for c in combinations(spots, 2):
        diff = (c[0][0] - c[1][0], c[0][1] - c[1][1])
        antinodes.append((tuple(map(lambda x, y: x + y, c[0], diff))))
        antinodes.append((tuple(map(lambda x, y: x - y, c[1], diff))))

# careful, have to be sorted or else we skip over elements
for n in sorted(antinodes):
    if n[0] < 0 or n[1] < 0 or n[0] >= size[0] or n[1] >= size[1]:
        antinodes.remove(n)

print(nodes)
print("antinodes")
print(sorted(antinodes))
print(f"part 1: number of antinodes: {len(set(antinodes))}")


def in_grid(n):
    global size
    if n[0] < 0 or n[1] < 0 or n[0] >= size[0] or n[1] >= size[1]:
        return False
    return True


antinodes = []
for n in nodes.keys():
    spots = nodes[n]
    for c in combinations(spots, 2):
        diff = (c[0][0] - c[1][0], c[0][1] - c[1][1])
        a = tuple(map(lambda x, y: x + y, c[0], diff))
        d = list(diff)
        while in_grid(a):
            antinodes.append(a)
            d = [d[0] + diff[0], d[1] + diff[1]]
            a = tuple(map(lambda x, y: x + y, c[0], d))
        b = tuple(map(lambda x, y: x - y, c[1], diff))
        d = list(diff)
        while in_grid(b):
            antinodes.append(b)
            d = [d[0] + diff[0], d[1] + diff[1]]
            b = tuple(map(lambda x, y: x - y, c[1], d))

for n in nodes.keys():
    spots = nodes[n]
    if len(spots) > 1:
        for j in spots:
            antinodes.append(j)

print(nodes)
print("antinodes")
print(sorted(antinodes))

for n in antinodes:
    grid[n[0]] = replace_char_in_str(grid[n[0]], n[1], '#')

for n in nodes.keys():
    for x in nodes[n]:
        grid[x[0]] = replace_char_in_str(grid[x[0]], x[1], n)

pprint(grid)

print(f"part 2: number of antinodes: {len(set(antinodes))}")
