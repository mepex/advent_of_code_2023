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


def get_lines(f):
    with open(f) as fp:
        lines = [line.rstrip() for line in fp]
    return lines


def replace_char_in_str(s, index, ch):
    return s[:index] + ch + s[index + 1:]


