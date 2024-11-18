import numpy as np

import pandas as pd
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

np.set_printoptions(threshold=np.inf)


with open("input.txt") as fp:
    lines = [line.strip() for line in fp]
    x = len(lines[0])
    y = len(lines)

grid = np.full((x, y), -1)

j = 0
with open("input.txt") as fp:
    for line in fp:
        for i in range(len(line.strip())):
            grid[i, j] = int(line[i])
        j += 1

print(grid)
print(f"size: {x} by {y}, {x*y} total")

hidden_trees = 0
for i in range(1, x-1):
    for j in range(1, y-1):
        height = grid[i, j]
        west = grid[:i, j]
        east = grid[i+1:, j]
        north = grid[i, :j]
        south = grid[i, j+1:]
        # if any tree in any direction is taller than the object tree, it's hidden in that direction
        # if a tree is hidden in all directions, it's a hidden tree
        if height <= np.amax(west) and \
            height <= np.amax(east) and \
            height <= np.amax(north) and \
            height <= np.amax(south):
            print(f"({i},{j}) : {height} is hidden")
            hidden_trees += 1

visible_trees = x * y - hidden_trees
print(f"part one: {visible_trees} are visible")

scenic = np.full((x, y), 0)
look_i = 14
look_j = 49

for i in range(1, x-1):
    for j in range(1, y-1):
        height = grid[i, j]
        if i == look_i and j == look_j:
            print(f"***XY = {i},{j} height: {height}")
        west = 0
        east = 0
        north = 0
        south = 0
        # look west
        for a in range(i-1, -1, -1):
            west += 1
            v = grid[a, j]
            if i == look_i and j == look_j:
                print(f"west: ({a},{j}) : {v}")
            if v >= height:
                break
        # look east
        for a in range(i + 1, x, 1):
            east += 1
            v = grid[a, j]
            if i == look_i and j == look_j:
                print(f"east: ({a},{j}) : {v}")
            if v >= height:
                break
        # look north
        for a in range(j-1, -1, -1):
            north += 1
            v = grid[i, a]
            if i == look_i and j == look_j:
                print(f"north: ({i},{a}) : {v}")
            if v >= height:
                break
        # look south
        for a in range(j+1, y, 1):
            south += 1
            v = grid[i, a]
            if i == look_i and j == look_j:
                print(f"south: ({i},{a}) : {v}")
            if v >= height:
                break
        s = north * south * east * west
        scenic[i, j] = s
        if s == 405769:
            print(f"scenic: {i},{j} : {west} {east} {north} {south} :: {s}")
        if i == look_i and j == look_j:
            print(f"scenic: {i},{j} : {west} {east} {north} {south} :: {s}")

#print(scenic)
print(f"part two- maximum scenic value: {np.max(scenic)}")
print(np.unravel_index(np.argmax(grid), grid.shape))










