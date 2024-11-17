import re
import numpy as np
import math
from functools import cache

f = "input.txt"

grid = []

def eval_line(m):
    n = []
    last = False
    i = 0
    for c in m:
        if c == "#":
            i += 1
        elif c == ".":
            if i > 0:
                n.append(i)
                i = 0
        else:
            return None
    if i > 0:
        n.append(i)
    return n

def replace_qs(m, i, size):
    s = bin(i)[2:].zfill(size)
    r = ''
    j = 0
    for i in range(len(m)):
        if m[i] == '?':
            r += '.' if s[j] == '0' else '#'
            j += 1
        else:
            r += m[i]
    return r


def process_line(m, g):
    q = m.count('?')
    if q == 0:
        return None
    p = 0
    for i in range(2**q):
        m2 = replace_qs(m, i, q)
        e = eval_line(m2)
        if e == g:
            p += 1
    return p


def process_line2(m, g):
    match = re.findall(r"[?#]+", m)
    v = 1
    for i in range(len(match)):
        pass

# ? could match 1
# ?? could match 1 or 2
# ??? could match 1 or 2 or 3 or 1,1
# ???? could match 1 or 2 or
def configuration_count(row: str, groups) -> int:
    def valid_group(start, length):
        valid = row[start:start + length].count('.') == 0
        valid = valid and len(row[start:start + length]) == length
        valid = valid and (start + length >= len(row) or row[start + length] in '.?')
        return valid

    @cache
    def recur(position, group_id):
        if group_id == len(groups):
            return row[position:].count('#') == 0
        if position >= len(row):
            return 0
        if row[position] == '#':
            if valid_group(position, groups[group_id]):
                return recur(position + groups[group_id] + 1, group_id + 1)
            else:
                return 0
        if valid_group(position, groups[group_id]):
            return (recur(position + groups[group_id] + 1, group_id + 1)
                    + recur(position + 1, group_id))
        return recur(position + 1, group_id)
    return recur(0, 0)


def timesn(m, g, n):
    m2 = (m + '?') * (n-1) + m
    g2 = g * n
    return m2, g2


with open(f) as fp:
    i = 0
    t1 = 0
    t2 = 0
    t5 = 0
    for line in fp:
        line = line.strip()
        result = re.search(r"([.#?]+) (.*)", line)
        if result:
            # print(result.groups())
            m = result.group(1)
            g = [int(x) for x in result.group(2).split(',')]
            n = eval_line(m)
            if n:
                print(f"eval: {n}, match = {n == g}")
            t = configuration_count(m, g)
            print(f"{m} : {g} has {t} possibilities")
            t1 += t
            m2, g2 = timesn(m, g, 5)
            t2 = configuration_count(m2, g2)
            #factor = int(t2/t)
            #times5 = t * (factor**4)
            print(f"  5x {m} : {g} has {t2} possibilities")
            t5 += t2


print(f"Part 1: {t1} possibilities")
print(f"Part 2: {t5} possibilities")



a = "?###????????"
b =  [3,2,1]
print(f"{a} : {b} ->> {process_line(a, b)}")
a1, b1 = timesn(a,b,2)
print(f"{a1} : {b1} ->> {process_line(a1, b1)}")
a1, b1 = timesn(a,b,3)
#print(f"{a1} : {b1} ->> {process_line(a1, b1)}")
#a1, b1 = timesn(a,b,4)
#print(f"{a1} : {b1} ->> {process_line(a1, b1)}")





