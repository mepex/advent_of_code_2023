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


f = "input.txt"
grid = []

def shift_line(row):
    # shift 0s to left, stopping at #s
    size = len(row)
    for i in range(0, size):
        for j in range(0, size - i - 1):
            a = row[j]
            b = row[j+1]
            if row[j] == "." and row[j + 1] == "O":
                row[j] = "O"
                row[j+1] = '.'
    return row

def matrix_print(a):
    print("\n".join(["".join([i for i in row]) for row in a]))

@timer_func
def orient_matrix(u, d):
    r = d % 4
    return np.rot90(u, k = r)

@timer_func
def shift_all(uni):
    for i in range(len(uni)):
        uni[i] = shift_line(uni[i])

@timer_func
def shift_rocks(uni, rotate):
    uc = np.copy(uni)
    uni_y = np.rot90(uc)
    i = 0

    shift_all(uni)

    d = -1
    while rotate > 0:
        d += 1
        uni_y = np.rot90(uni_y, k=-1)
        shift_all(uni)
        rotate -= 1
        #matrix_print(orient_matrix(uni_y, d))
        #print("\n")

    uni2 = orient_matrix(uni_y, d)
    #matrix_print(uni2)
    return uni2

def find_weight(uni2):
    total = 0
    for i in range(len(uni2)):
        weight = len(uni2) - i
        line_weight = weight * list(uni2[i]).count("O")
        total += line_weight
    return total


s = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            grid.append([x for x in line])

if grid:
    uni = np.array([np.array(xi) for xi in grid])
    uni2 = shift_rocks(uni, 0)
    matrix_print(uni2)
    s = find_weight(uni2)
    print(f"Part 1: {s}")


def find_oscillation(l):
    i = 0
    length = 1
    d = 0

    repeats = [x for x, n in enumerate(l) if n == l[-1]]

    for j in range(1, len(repeats)):
        if len(repeats) >= 2*j + 1:
            idx1 = -1 * (j+1)
            idx2 = -1 * (2*j + 1)
            d1 = repeats[-1] - repeats[idx1]
            d2 = repeats[idx1] - repeats[idx2]
            if d1 == d2:
                for k in range(repeats[j-2], repeats[j-1]):
                    if l[k] != l[k+d1]:
                        return None
                return d1
    return None


p = find_oscillation([1,2,3,4,5,6,7,8,9,6,7,8,6,7,8,9,6,7,8,6,7,8,9,6])
print(f"osc = {p}")

w = []
find = 0
cycles = 1
uni_test = shift_rocks(uni, 3)

while cycles < 1000:
    uni_test = shift_rocks(uni_test, 3)
    weight = find_weight(uni_test)
    w.append(weight)
    print(f"{weight},", end='')
    cycles += 1
    if len(w) > 50:
        p = find_oscillation(w)
        if p:
            break

print(f"cycle of length {p} at cycles {cycles}")
print(f"cycle is\n {w[-p:]}")





# 1 cycle
# uni_test = shift_rocks(uni, 399)
# print("250 cycles:")
# matrix_print(uni_test)
# find = 0
# cycles = 1
# last_match = 0
# weight = []
# cycle_time = 0
# u_test = np.copy(uni)
# while find < 10 and cycles < 5000:
#     u_test = shift_rocks(u_test, 3)
#     w = find_weight(uni_test)
#     weight.append(w)
#     print(f"{w},", end='')
#     if np.array_equal(u_test, uni_test):
#         cycle_time = cycles-last_match
#         print(f"\nfound match at {cycles} cycles, cycle_time is {cycles - last_match}, {w}")
#         last_match = cycles
#         find += 1
#     cycles += 1
#
# for i in range(2 * cycle_time):
#     u_fish = shift_rocks(uni, (i*4) + 100 - 1)
#     print(find_weight(u_fish))

# a billion is equivalent to







