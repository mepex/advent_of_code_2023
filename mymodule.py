import numpy as np


def get_grid_of_chars(f):
    grid = []
    with open(f) as fp:
        i = 0
        for line in fp:
            line = line.strip()
            grid.append(line)
    return grid


def get_grid_of_ints(f):
    grid = []
    with open(f) as fp:
        for line in fp:
            grid.append([int(x) for x in line.split()])
    return np.array(grid)

def get_grid_of_digits(f):
    grid = []
    with open(f) as fp:
        for line in fp:
            grid.append([int(x) for x in list(line.strip())])
    return np.array(grid)


def get_lines(f):
    with open(f) as fp:
        lines = [line.rstrip() for line in fp]
    return lines


def replace_char_in_str(s, index, ch):
    return s[:index] + ch + s[index + 1:]


def get_grid_neighbors(shape, y, x):
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

def flood_fill(pos):
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
                p, a = flood_fill(n)
                area += a
                perim += p
    return perim, area


