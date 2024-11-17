import re
import numpy as np
import math
from functools import cache
from time import time
import sys
from treelib import Node, Tree


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

def matrix_print(a):
    print("\n".join(["".join([f"{i:<1}" for i in row]) for row in a]))


def travel(grid, start, step, finalstep = 6):

    y, x = start
    rows = len(grid)
    cols = len(grid[0])
    grid[y][x] = step
    if step == finalstep:
        return
    if y > 0 and grid[y-1][x] != '#':
        travel(grid, (y-1, x), step+1, finalstep)
    if y < cols-1 and grid[y+1][x] != '#':
        travel(grid, (y+1, x), step+1, finalstep)
    if x > 0 and grid[y][x-1] != '#':
        travel(grid, (y, x-1), step+1, finalstep)
    if x < rows-1 and grid[y][x+1] != '#':
        travel(grid, (y, x+1), step+1, finalstep)


def travel_tree(parent, start, step, finalstep = 64):
    global grid, tree
    y, x = start
    rows = len(grid)
    cols = len(grid[0])
    if not tree.contains(str(start)):
        tree.create_node(str(start), str(start), parent=str(parent))
    if step == finalstep:
        return
    if y > 0 and grid[y - 1][x] != '#' and not tree.contains(str((y-1,x))):
    # if y > 0 and grid[y - 1][x] != '#':
        travel_tree(str(start), (y - 1, x), step + 1, finalstep)
    if y < cols - 1 and grid[y + 1][x] != '#' and not tree.contains(str((y+1,x))):
    # if y < cols - 1 and grid[y + 1][x] != '#':
        travel_tree(str(start), (y + 1, x), step + 1, finalstep)
    if x > 0 and grid[y][x - 1] != '#' and not tree.contains(str((y,x-1))):
    #  if x > 0 and grid[y][x - 1] != '#':
        travel_tree(str(start), (y, x - 1), step + 1, finalstep)
    if x < rows - 1 and grid[y][x + 1] != '#' and not tree.contains(str((y,x+1))):
    # if x < rows - 1 and grid[y][x + 1] != '#':
        travel_tree(str(start), (y, x + 1), step + 1, finalstep)





sys.setrecursionlimit(1000000)
f = "input.txt"
grid = []
start = None
i = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            grid.append([x for x in line])
        if 'S' in line:
            start = (i, line.index('S'))
        i += 1


if grid:
    tree = Tree()
    tree.create_node(str(start), str(start))  # root node
    finalcount = 64
    travel_tree(str(start), start, 0, finalcount)
    print(f"tree stats: start: {start} depth: {tree.depth()} nodes: {len(tree)}")
    #divisors of 64 are 2,4,8,16,32,64
    print(f"root depth: {tree.depth(str(start))}")
    print(f"contains 1,65 {tree.contains(str((65,1)))}")
    divs = [1,2,4,8,16,32,64]
    total= 0
    for n in tree.nodes:
        y, x = eval(n)
        grid[y][x] = '*'
        if tree.depth(n) % 2 == 0:
            total += 1
    grid[start[0]][start[1]] = 'S'
    print(f"part 1 total: {total}")
    matrix_print(grid)

