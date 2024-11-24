import re
from itertools import permutations

f = "input.txt"
weights = {}
count = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.search(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)', line)
        if m:
            a = m.group(1)
            sign = 1 if m.group(2) == "gain" else -1
            b = m.group(4)
            if not a in weights.keys():
                weights[a] = {}
            weights[a][b] = sign * int(m.group(3))

def calc_weight(arr, weights):
    s = len(arr)
    w = 0
    for i in range(s):
        a = arr[i]
        b = arr[(i+1) % s]
        w += weights[a][b]
        w += weights[b][a]
    return w


names = weights.keys()
baseline = calc_weight(list(names), weights)

perms = permutations(names, len(names))
vals = []
for p in perms:
    vals.append(calc_weight(p, weights))

print(max(vals))

weights['ME'] = {}
for n in names:
    weights[n]['ME'] = 0
    weights['ME'][n] = 0

perms = permutations(names, len(names))
vals = []
for p in perms:
    vals.append(calc_weight(p, weights))

print(max(vals))


