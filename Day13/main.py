import re
import numpy as np
import math
from functools import cache
from itertools import chain
from itertools import combinations

f = "input.txt"

grid = []

def num_differences(l1, l2, threshold=1):
    t = 0
    for i in range(len(l1)):
        t = t + 1 if l1[i] != l2[i] else t
        if t > threshold:
            return t
    return t


def has_reflection(grid, arr, n, smudge=False):
    # try all possible centers
    for i in range(len(grid)-1):
        if not smudge and num_differences(grid[i], grid[i+1]) == 1:
            s = has_reflection(grid, [[i, i+1]] + arr, n, True)
            if s:
                return s

    center = []

    for a in arr:
        if a[1] - a[0] == 1:
            center.append(list(a))


    s = []
    for s in center:
        clist = s
        c = s[0] + 1
        while s in arr:
            s = [s[0]-1, s[1] + 1]
        if s[0] == -1 or s[1] == n:
            if smudge:
                return c
            else:
                arr.remove(clist)
        elif not smudge and num_differences(grid[s[0]], grid[s[1]]) == 1:
            r = has_reflection(grid, [s] + arr, n, True)
            if r:
                return r


def make_pairs(arr):
    i = 0
    while i < len(arr):
        a = arr[i]
        # if there are more than two identical rows, enumerate them
        if len(a) > 2:
            comb = combinations(a, 2)
            for c in comb:
                arr.append(list(c))
            arr.remove(a)
        else:
            i += 1
    return arr


def check_grid(uni):
    rows, cols = uni.shape
    unq, count = np.unique(uni, axis=0, return_counts=True)
    # print(f"unique x: {unq}, {count}")
    repeated_groups = unq[count > 1]
    repeats = []
    for repeated_group in repeated_groups:
        repeated_idx = np.argwhere(np.all(uni == repeated_group, axis=1))
        # print(repeated_idx.ravel())
        repeats.append(list(repeated_idx.ravel()))

    flatten_list = list(chain.from_iterable(repeats))
    # if repeats contains all rows it has a mirror
    repeats = make_pairs(repeats)
    #print(f"x repeats: {repeats}, rows: {rows}")
    c = has_reflection(uni, repeats, rows)
    if c:
        return c
    return None


def find_mirrors(grid):
    summary = 0
    c = d = 0
    uni = np.array([np.array(xi) for xi in grid])
    c = check_grid(uni)
    # rotate 90 degrees clockwise to process y axis
    uni_y = np.rot90(uni, k=-1)
    d = check_grid(uni_y)
    if c:
        print(f"x reflection at {c * 100}")
        return c * 100
    if d:
        print(f"y reflection at {d}")
        return d
    if summary == 0:
        print("FAIL!!")
        print(np.array([np.array(xi) for xi in grid]))
        print()
        print(np.rot90(np.array([np.array(xi) for xi in grid]), k=-1))
        exit(-1)
    return summary

sum = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            grid.append([x for x in line])
        else:
            sum += find_mirrors(grid)
            grid = []
    if grid:
        sum += find_mirrors(grid)

print(f"part 1: {sum}")








