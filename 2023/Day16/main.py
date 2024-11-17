import re
import numpy as np
import math
from functools import cache
from time import time


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


# look-up table for what the pipes do depending on the direction traveled
m = {
    'e' : {
        '.' : 'e',
        '/' : 'n',
        '\\' : 's',
        '-' : 'e',
        '|' : 'ns'
    },
    's' : {
        '.' : 's',
         '/' : 'w',
        '\\' : 'e',
        '-' : 'ew',
        '|' : 's'
    },
    'w' : {
        '.' : 'w',
        '/' : 's',
        '\\': 'n',
        '-': 'w',
        '|': 'ns'
    },
    'n' : {
            '.' : 'n',
            '/' : 'e',
            '\\': 'w',
            '-': 'ew',
            '|': 'n'
        }
}

def next_coord(coord, dir):
    y,x = coord
    if dir == 'e':
        return (y, x+1)
    if dir == 'n':
        return (y-1, x)
    if dir == 's':
        return (y+1, x)
    if dir == 'w':
        return (y, x-1)

def follow_beam(coord, dir):
    global uni
    global visited
    global m
    y,x = coord

    while x in range(len(uni[0])) and y in range(len(uni)) and dir not in visited[y][x]:
        ch = uni[y, x]
        visited[y][x] += dir
        next = m[dir][ch]
        if len(next) == 2:
            visited[y][x] += next[0]
            print(f"split at {y},{x} : {next[0]}, visited: {visited[y][x]}")
            follow_beam(next_coord((y,x), next[0]), next[0])
            visited[y][x] += next[1]
            print(f"other split at {y},{x} : {next[1]}, visited: {visited[y][x]}")
            follow_beam(next_coord((y,x), next[1]), next[1])
        else:
            dir = next
            y,x = next_coord((y,x), next)
            print(f"going {dir} to {y},{x}")


def follow_beam2(coord, dir):
    global uni
    global visited
    global m
    y,x = coord
    if x in range(len(uni[0])) and y in range(len(uni)) and dir not in visited[y][x]:
        ch = uni[y, x]
        visited[y][x] += dir
        next = m[dir][ch]
        if len(next) == 2:
            visited[y][x] += next[0]
            print(f"split at {y},{x} : {next[0]}, visited: {visited[y][x]}")
            follow_beam2(next_coord((y,x), next[0]), next[0])
            visited[y][x] += next[1]
            print(f"other split at {y},{x} : {next[1]}, visited: {visited[y][x]}")
            follow_beam2(next_coord((y,x), next[1]), next[1])
        else:
            follow_beam2(next_coord((y,x), next), next)


def make_v(visited):
    y = len(visited)
    x = len(visited[0])
    v = np.zeros((y,x), dtype=int)
    for y in range(len(visited)):
        for x in range(len(visited[y])):
           if visited[y][x] != "":
               v[y,x] = 1
           else:
                v[y,x] = 0
    return v




def matrix_print(a):
    print("\n".join(["".join([str(i) for i in row]) for row in a]))

def get_tile_count(visited):
    make_v(visited)
    size = uni.shape[0] * uni.shape[1]
    unique, counts = np.unique(visited, return_counts=True)
    dcounts = dict(zip(unique, counts))
    return size - dcounts['']

f = "input.txt"
grid = []


with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            grid.append([x for x in line])

if grid:
    uni = np.array([np.array(xi) for xi in grid])
    y, x = uni.shape
    visited = [ ['']*x for i in range(y)]
    follow_beam((0,0),'e')
    matrix_print(uni)
    print('---')
    print(f"part 1: {get_tile_count(visited)}")

tiles = []
rows, cols = uni.shape

for i in range(rows):
    visited = [[''] * x for i in range(y)]
    follow_beam((0,i), 's')
    tiles.append(get_tile_count(visited))

for i in range(rows):
    visited = [[''] * x for i in range(y)]
    follow_beam((cols-1,i), 's')
    tiles.append(get_tile_count(visited))

for j in range(cols):
    visited = [[''] * x for i in range(y)]
    follow_beam((j, 0), 's')
    tiles.append(get_tile_count(visited))

for j in range(cols):
    visited = [[''] * x for i in range(y)]
    follow_beam((j, rows-1), 's')
    tiles.append(get_tile_count(visited))

print(f"Part 2: {max(tiles)}")










