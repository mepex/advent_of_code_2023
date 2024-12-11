from mymodule import *
import re

lines = get_lines("sample.txt")
d = [int(x) for x in lines[0].split()]


def blink(d: list):
    i = 0
    while i < len(d):
        n = d[i]
        if n == 0:
            d[i] = 1
        elif not len(str(n)) % 2:
            l = len(str(n))
            n1 = int(str(n)[:l // 2])
            n2 = int(str(n)[l // 2:])
            d.insert(i, n1)
            d[i + 1] = n2
            i += 1
        else:
            d[i] = n * 2024
        i += 1

for i in range(25):
    blink(d)
print(f"part 1: {len(d)}")

memo = []




