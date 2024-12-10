from mymodule import *
from pprint import pprint
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def find_trailheads(grid):
    th = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                th.append((y, x))
    return th

def find_summits(grid):
    s = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 9:
                s.append((y, x))
    return s


def get_neighbors(shape, y, x):
    n = []
    # left
    n.append((y, max(x - 1, 0)))
    # right
    n.append((y, min(x + 1, shape[0] - 1)))
    # up
    n.append((max(0, y - 1), x))
    # down
    n.append((min(y + 1, shape[0] - 1), x))
    while (y, x) in n:
        n.remove((y, x))
    return list(set(n))


def find_trails(grid: np.array, y, x, g: nx.Graph):
    """
    Create a graph that has finds all the paths to a summit
    :param grid:
    :param y:
    :param x:
    :param g:
    :return:
    """
    b = y
    a = x
    v = grid[b][a]
    n = v + 1
    for j, i in get_neighbors(grid.shape, b, a):
        if grid[j][i] == n:
            if not (b, a) in g.nodes:
                g.add_node((b, a))
            if not (j, i) in g.nodes:
                g.add_node((j, i))
            g.add_edge((b, a), (j, i))
            find_trails(grid, j, i, g)


grid = get_grid_of_digits("input.txt")
trailheads = find_trailheads(grid)
summits = find_summits(grid)
pprint(grid)
pprint(trailheads)


score = 0
score2 = 0
for th in trailheads:
    # need a directed graph otherwise we'll go around loops
    g = nx.DiGraph()
    find_trails(grid, th[0], th[1], g)
    tops = set()
    rating = 0
    for s in summits:
        if s in g.nodes:
            for p in nx.all_simple_paths(g, th, s):
                rating += 1
                tops.add(p[-1])
    print(f"found {len(tops)} summits starting at {th}")
    print(f"found {rating} paths to summit {s} from {th}")
    score += len(tops)
    score2 += rating
    print("")

print(f"part 1: {score}")
print(f"part 2: {score2}")

