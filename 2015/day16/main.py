import re
from collections import defaultdict

f = "input.txt"
weights = {}
count = 0
sues = []
sues.append(defaultdict(lambda: -1))
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.findall(r'(\w+): (\d+)', line)
        if m:
            sues.append(defaultdict(lambda: -1))
            for s in m:
                sues[-1][s[0]] = int(s[1])

constraints = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


for i in range(1, len(sues)):
    found = True
    for k,v in constraints.items():
        s = sues[i]
        val = s[k]
        if val != v and val != -1:
            found = False
            break
    if found:
        print(f"part 1: found: {i} : {sues[i]}")

for i in range(1, len(sues)):
    found = True
    for k,v in constraints.items():
        s = sues[i]
        val = s[k]
        if k == "cats" or k == "trees":
            if val <= v and val != -1:
                found = False
                break
        elif k == "pomeranians" or k == "goldfish":
            if val >= v and val != -1:
                found = False
                break
        else:
            if val != v and val != -1:
                found = False
                break
    if found:
        print(f"part 1: found: {i} : {sues[i]}")




