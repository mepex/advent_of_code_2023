import re
import numpy as np
import math

f = "input.txt"

grid = []




def expand_universe(universe):
    rows, cols = universe.shape
    x = y = 0
    while x < rows:
        row = list(universe[x, :])
        if row.count('.') == cols:
            universe = np.insert(universe, x, '.', axis=0)
            print(f"inserting row at {x}")
            rows, cols = universe.shape
            x += 2
        else:
            x += 1

    while y < cols:
        col = list(universe[:,y])
        if col.count('.') == rows:
            universe = np.insert(universe, y, '.', axis=1)
            print(f"inserting col at {y}")
            rows, cols = universe.shape
            y += 2
        else:
            y += 1
    return universe

def find_galaxies(universe):
    g = []
    for idx, val in np.ndenumerate(universe):
        if val == '#':
            g.append(idx)
    return g

def find_distances(g):
    total = 0
    for x in range(len(g)):
        a = g[x]
        for y in range(x+1,len(g)):
            b = g[y]
            d = abs(a[0] - b[0]) + abs(a[1] - b[1])
            total += d
    return total


with open(f) as fp:
    i = 0
    for line in fp:
        line = line.strip()
        grid.append([x for x in line])
        i = i + 1

universe = np.array([np.array(xi) for xi in grid])
universe = expand_universe(universe)

print(universe)
g = find_galaxies(universe)
print(g)
d = find_distances(g)
print(d)

def expand_universe_x(universe):
    rows, cols = universe.shape
    x_rows = []
    x_cols = []
    x = y = 0
    while x < rows:
        row = list(universe[x, :])
        if row.count('.') == cols:
            universe = np.insert(universe, x, 'X', axis=0)
            print(f"inserting row at {x}")
            x_rows.append(x)
            rows, cols = universe.shape
            x += 2
        else:
            x += 1

    while y < cols:
        col = list(universe[:,y])
        if col.count('.') + col.count('X') == rows:
            universe = np.insert(universe, y, 'X', axis=1)
            print(f"inserting col at {y}")
            x_cols.append(y)
            rows, cols = universe.shape
            y += 2
        else:
            y += 1
    return universe, x_rows, x_cols

universe = np.array([np.array(xi) for xi in grid])
universe, x_rows, x_cols = expand_universe_x(universe)
print(universe)

def find_distances_x(g, x_rows, x_cols, s=1000):
    total = 0
    for x in range(len(g)):
        a = g[x]
        for y in range(x+1,len(g)):
            b = g[y]
            d = abs(a[0] - b[0]) + abs(a[1] - b[1])
            r = range(a[0], b[0]) if a[0] <= b[0] else range(b[0], a[0])
            for i in x_rows:
                if i in r:
                    d += s-1
            r = range(a[1], b[1]) if a[1] <= b[1] else range(b[1], a[1])
            for i in x_cols:
                if i in r:
                    d += s-1
            print(f"{a} to {b} : {d}")
            total += d
    return total

d = find_distances_x(g, x_rows, x_cols, 999999)
print(d)