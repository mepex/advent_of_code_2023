import re
from collections import Counter

f = ("input.txt")
a = []
b = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.match(r'(\d+)\s+(\d+)', line)
        if m:
            a.append(int(m.group(1)))
            b.append(int(m.group(2)))

a_s = sorted(a)
b_s = sorted(b)

diff = 0
for i in range(len(a_s)):
    diff += abs(a_s[i] - b_s[i])

print(f"part 1: diff = {diff}")

b_c = Counter(b_s)

score = 0
for n in a:
    score += b_c[n] * n

print(f"part 2 score = {score}")
