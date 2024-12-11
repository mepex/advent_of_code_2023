from mymodule import *
from collections import Counter

lines = get_lines("input.txt")
golden = [int(x) for x in lines[0].split()]


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

def blink2(d: Counter):
    c = Counter()
    ks = list(d)
    for k in ks:
        v = d[k]
        if k == 0:
            c[1] = v if 1 not in c else v + c[1]
        elif not len(str(k)) % 2:
            l = len(str(k))
            n1 = int(str(k)[:l // 2])
            n2 = int(str(k)[l // 2:])
            c[n1] = v if n1 not in c else v + c[n1]
            c[n2] = v if n2 not in c else v + c[n2]
        else:
            c[k * 2024] = v if k*2024 not in c else v + c[n*2024]
    return c



d = Counter(golden)
d1 = golden.copy()
for i in range(25):
    d = blink2(d)

print(f"part 1: {sum(d.values())}")

for i in range(55):
    d = blink2(d)

print(f"part 2: {sum(d.values())}")






