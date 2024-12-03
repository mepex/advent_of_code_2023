import re

f = ("input.txt")
total = 0
lines = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        lines.append(line)
        m = re.findall(r'mul\((\d+),(\d+)\)', line)
        for n in m:
            a = int(n[0])
            b = int(n[1])
            total += a * b

print(f"part 1: {total}")

total = 0
do = True
for line in lines:
    m = re.findall(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))', line)
    for n in m:
        if n[0] == 'don\'t()':
            do = False
        elif n[0] == 'do()':
            do = True
        elif n[1] and do:
            a = int(n[1])
            b = int(n[2])
            total += a * b

print(f"part 2: {total}")

