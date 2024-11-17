import re
import numpy as np
import math
from functools import cache
from time import time
from djikstra import *
import sys


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


def next_dest(grid, source, dir):
    sy, sx = source.split(',')
    sy = int(sy)
    sx = int(sx)
    rows = len(grid)
    cols = len(grid[0])
    next = []
    for i in range(1,4):
        if dir == 'e' and sx+i < cols:
            next.append(f"{sy},{sx+i}")
        elif dir == 's' and sy+i < rows:
            next.append(f"{sy+i},{sx}")
        elif dir == 'n' and sy-i > 0:
            next.append(f"{sy - i},{sx}")
        elif dir == 'w' and sx-i > 0:
            next.append(f"{sy},{sx-i}")
    return next


def build_local_edge(grid, source, dest, dir) -> int:
    sy, sx = map(int, source.split(','))
    dy, dx = map(int, dest.split(','))
    w = 0
    if dir == 'e':
        for i in range(sx+1, dx+1):
            w += grid[sy][i]
    if dir == 'w':
        for i in range(dx, sx, -1):
            w += grid[sy][i]
    if dir == 'n':
        for i in range(dy, sy, -1):
            w += grid[i][sx]
    if dir == 's':
        for i in range(sy+1, dy+1):
            w += grid[i][sx]
    return w


#
#  The way to constrain the legal path is to constrain the edge list.  From node y,x, if the travel is in the y
#  direction, the only nodes connected to that node go in the x direction, and vice versa. So for 0,0
#  0,0 -> 0,1 = a
#  0,0 -> 0,2 = a+b
#  0,0 -> 0,3 = a+b+c
#  0,0 -> 0,4 = not in list
#  0,0 -> 1,0 = d
#  0,0 -> 2,0 = d+e
#  0,0 -> 3,0 = d+e+f
#  0,0 -> 4,0 = infinite
#
def build_edges(grid, source, dir) -> list:
    global edgeset, final
    sourcenode = f"{source},{dir}" if source != "0,0" else "0,0"
    if source == final:
        return None
    if sourcenode in edgeset:
        return None
    edgeset.add(sourcenode)
    edgelist = []
    sy, sx = map(int, source.split(','))
    legal = []
    next_dirs = {'e' : 'ns', 'w' : 'ns', 'n' : 'ew', 's' : 'ew'}
    nd = next_dest(grid, source, dir)
    for n in nd:
        dy, dx = map(int, n.split(','))
        destnode = f"{dy},{dx},{dir}" if n != final else final
        legal.append((sourcenode, destnode, build_local_edge(grid, source, n, dir)))
        a = build_edges(grid, n, next_dirs[dir][0])
        b = build_edges(grid, n, next_dirs[dir][1])
        if a :
            legal.extend(a)
        if b:
            legal.extend(b)
    return legal


def build_edges_simple(grid):
    edgelist = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            edgesource = f"{y},{x}"
            # up to four possible edges, n, e, s, w
            if x > 0:
                edgelist.append((edgesource, f"{y},{x-1}", grid[y][x]))
            edgelist.append((edgesource, f"{y},{x + 1}", grid[y][x]))
            if y > 0:
                edgelist.append((edgesource, f"{y-1},{x}", grid[y][x]))
            edgelist.append((edgesource, f"{y+1},{x}", grid[y][x]))
    return edgelist

def build_nodes(cols, rows):
    nodelist = []
    for y in range(cols):
        for x in range(rows):
            nodelist.append(f"{y},{x}")
    return nodelist


f = "testinput2.txt"
grid = []

sys.setrecursionlimit(10000)

with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            grid.append([int(i) for i in line])

edgeset = set()
edgelist = []
if grid:
    rows = len(grid)
    cols = len(grid[0])
    final = f"{rows-1},{cols-1}"
    edgelist = build_edges(grid, "0,0", 'e')
    # nodelist = build_nodes(cols, rows)
    g = build_graph(edgelist)
    dest = f"{rows-1},{cols-1}"
    print("=== Dijkstra ===")

    print("--- Single source, single destination ---")
    d, prev = dijkstra(g, "0,0", dest)
    path = find_path(prev, dest)
    print(f"0,0 -> {dest}: distance = {d}, path = {path}")


