from mymodule import *
from copy import deepcopy
import numpy as np

grid = get_grid_of_chars('input.txt')
grid_shape = len(grid), len(grid[0])
visited = []
for i in range(grid_shape[0]):
    visited.append([0] * grid_shape[1])

blank = deepcopy(visited)

def get_next(last):
    global visited
    for j in range(last[0], len(visited)):
        for i in range(len(visited[0])):
            if not visited[j][i]:
                return j, i
    return -1, -1


def get_island(pos):
    global grid, visited, grid_shape, region
    y = pos[0]
    x = pos[1]
    v = grid[y][x]
    visited[y][x] = 1
    region[y][x] = 1
    perim = 4
    area = 1
    for n in get_grid_neighbors(grid_shape, y, x):
        if grid[n[0]][n[1]] == v:
            perim -= 1
            if not visited[n[0]][n[1]]:
                p, a = get_island(n)
                area += a
                perim += p
    return perim, area

def find_sides(region):
    last = 0
    sides = 0
    # left to right
    # if we see a change, and the two pixels to the left of us aren't the same, or the pixel above isn't the same,
    # we have a corner, so increment the sides
    for j in range(len(region)):
        for i in range(len(region[0])):
            if last != region[j][i]:
                if (region[j-1][i-1] != region[j][i-1]) or (region[j][i] != region[j-1][i]):
                    sides += 1
            last = region[j][i]

    # top to bottom
    # if we see a change, and the two pixels above aren't the same, or the pixel to the left isn't the same,
    # we have a corner, so increment the sides
    for i in range(len(region[0])):
        for j in range(len(region)):
            if last != region[j][i]:
                if (region[j - 1][i - 1] != region[j-1][i]) or (region[j][i] != region[j][i-1]):
                    sides += 1
            last = region[j][i]
    return sides




next = 0, 0
price = 0
discount = 0
while next != (-1, -1):
    region = deepcopy(blank)
    p, a = get_island(next)
    # pad with zeros using np array
    r = np.zeros((grid_shape[0] + 2, grid_shape[1] + 2), dtype=int)
    # copy region into the middle, surrounded by zeros
    r[1:grid_shape[0] + 1, 1:grid_shape[1] + 1] = region
    s = find_sides(r)
    print(f"Found {grid[next[0]][next[1]]} at {next} area = {a} perim = {p}, sides = {s}")
    price += p * a
    discount += s * a
    next = get_next(next)

print(f"part 1: {price}")
print(f"part 2: discounted {discount}")
