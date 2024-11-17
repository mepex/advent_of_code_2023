import re
import numpy as np
import math

f = "input.txt"

# (y,x)
pipes = {
    '-' : [(0, -1), (0, 1)],
    '7' : [(0, -1), (1, 0)],
    '|' : [(-1, 0), (1, 0)],
    'J' : [(-1, 0), (0, -1)],
    'L' : [(0, 1), (-1, 0)],
    'F' : [(1, 0), (0, 1)]
}

def next_step(grid, origin, loc):
    if loc[0] < 0 or loc[1] < 0:
        return None, loc
    o = grid[origin[0]][origin[1]]
    l = grid[loc[0]][loc[1]]
    x_diff = origin[1] - loc[1]
    y_diff = origin[0] - loc[0]
    x = 0
    y = 0
    if l not in pipes:
        return None, loc
    p = pipes[l]
    try:
        idx = p.index((y_diff, x_diff))
    except ValueError:
        return None, loc
    n = p[0] if idx == 1 else p[1]
    new_loc = loc[0] + n[0], loc[1] + n[1]
    print(f"previous: {loc} -> {l} -> {new_loc}")
    return grid[new_loc[0]][new_loc[1]], new_loc




grid = []
total = 0
origin = (0,0)
with open(f) as fp:
    i = 0
    for line in fp:
        line = line.strip()
        grid.append([x for x in line])
        result = re.search('S', line)
        if result:
            origin = i, result.span()[0]
        i = i + 1


n = '.'
i = 0
a = origin[0]
b = origin[1]
# all directions from origin, find first step
first = [(a, b-1), (a, b+1), (a-1, b), (a+1, b)]
for d in first:
    n, loc = next_step(grid, origin, d)
    if n is not None:
        break
i = 2
prev = d
path = [origin, d, loc]
while n != 'S':
    n, new = next_step(grid, prev, loc)
    prev = loc
    loc = new
    path.append(new)
    i = i + 1
print(f"Found cycle, which is {i} steps, so furthest away is {i/2}")
print(f"path: {path}")

grid[origin[0]][origin[1]] = 'F'


for y in range(len(grid)):
    for x in range(len(grid[y])):
        if not (y,x) in path:
            grid[y][x] = "0"
    print(''.join(grid[y]))

print("\n")

cross = 0
interiors = 0
for y in range(len(grid)):
    corners = []
    for x in range(len(grid[y])):
        aa = grid[y][x]
        if aa in "|":
            cross += 1
        if aa in "FL":
            corners.append(aa)
        if len(corners) != 0:
            if aa == 'J' and corners[-1] == "F":
                cross += 1
                corners.pop(-1)
            if aa == "7" and corners[-1] == "L":
                cross += 1
                corners.pop(-1)
        if aa == "0" and cross % 2 == 1:
            interiors = interiors + 1
            grid[y][x] = "I"
    print(''.join(grid[y]))

print(f"total interior pixels: {interiors}")












