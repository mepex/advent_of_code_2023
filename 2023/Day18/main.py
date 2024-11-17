import re
import numpy as np
import math
from functools import cache
from time import time
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


def next_coord(coord, dir):
    y, x = coord
    if dir == 'e':
        return (y, x + 1)
    if dir == 'n':
        return (y - 1, x)
    if dir == 's':
        return (y + 1, x)
    if dir == 'w':
        return (y, x - 1)


def get_vertices(inst, starty, startx):
    v = []
    x, y = starty, startx
    maxx = 0
    maxy = 0
    minx = 100000000
    miny = 100000000
    for dir, length, color in inst:
        length = int(length)
        if dir == "R":
            x += length
        elif dir == 'U':
            y -= length
        elif dir == 'L':
            x -= length
        elif dir == 'D':
            y += length
        v.append((y, x))
        print(f"{dir}, {length} --> {y},{x}")
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        minx = min(minx, x)
        miny = min(miny, y)
    # now offset everything
    size = (maxy - miny + 1, maxx - minx + 1)
    start = (-miny, -minx)
    offset_v = []
    for c in v:
        offset_v.append((c[0] - miny, c[1] - minx))
    return size, start, offset_v


def get_dir_length(color):
    dir_l = ['R', 'D', 'L', 'U']
    length = int(color[2:7], 16)
    dir = dir_l[int(color[7])]
    return dir, length


def get_vertices_part2(inst, starty, startx):
    v = []
    x, y = starty, startx
    maxx = 0
    maxy = 0
    minx = 100000000
    miny = 100000000
    min_step_size = 10000000
    for dir, length, color in inst:
        dir, length = get_dir_length(color)
        min_step_size = min(min_step_size, length)
        if dir == "R":
            x += length + 1
        elif dir == 'U':
            y -= length + 1
        elif dir == 'L':
            x -= length + 1
        elif dir == 'D':
            y += length + 1
        v.append((y, x))
        print(f"{dir}, {length} --> {y},{x}")
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        minx = min(minx, x)
        miny = min(miny, y)
        # now offset everything
    size = (maxy - miny + 1, maxx - minx + 1)
    start = (-miny, -minx)
    offset_v = []
    for c in v:
        offset_v.append((c[0] - miny, c[1] - minx))
    return size, start, offset_v


def make_grid(size, start, v):
    grid = [['.'] * size[1] for i in range(size[0])]
    y, x = start
    for vy, vx in v:
        if vy == y:
            if vx > x:
                for i in range(x, vx + 1):
                    grid[y][i] = '#'
            else:
                for i in range(vx, x):
                    grid[y][i] = '#'
        else:
            if vy > y:
                for i in range(y, vy + 1):
                    grid[i][x] = '#'
            else:
                for i in range(vy, y):
                    grid[i][x] = "#"
        y, x = vy, vx
    return grid


def matrix_print(a):
    print("\n".join(["".join([str(i) for i in row]) for row in a]))


def flood_fill(grid, start):
    y, x = start
    if grid[y][x] == '.':
        grid[y][x] = '#'
        flood_fill(grid, (y, x + 1))
        flood_fill(grid, (y, x - 1))
        flood_fill(grid, (y + 1, x))
        flood_fill(grid, (y - 1, x))
    return grid


def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((y0, x0), (y1, x1)) in segments(p)))

def segments(p):
    return zip(p, p[1:] + [p[0]])



sys.setrecursionlimit(1000000)
f = "testinput.txt"
grid = []

inst = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            inst.append(tuple(line.split()))

size, start, v = get_vertices(inst, 0, 0)
print(size)
print(start)
print(v)
grid = make_grid(size, start, v)
matrix_print(grid)
grid = flood_fill(grid, (start[0] + 1, start[1] + 1))
print("\n----\n")
matrix_print(grid)
total = 0
for y in grid:
    total += y.count('#')
print(f"\nPart 1: {total}")
print(f"Alt Part 1: {area(v)}")

size, start, v = get_vertices_part2(inst, 0, 0)
v.insert(0, (0,0))
print(size)
print(start)
print(v)

#v.insert(0, (0,0))


print(f"part 2: {area(v)}")

area = 0;
#for (i = 0; i < n; i++) {


print(f"part 2: {area}")



# area += x[i+1]*(y[i+2]-y[i]) + y[i+1]*(x[i]-x[i+2]);
