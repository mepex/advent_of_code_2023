import re
import numpy
import math

f = "input.txt"

network = {}
with open(f) as fp:
    i = 0
    for line in fp:
        line = line.strip()
        if i == 0:
            directions = line
        elif line != "":
            result = re.match(r"([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)", line)
            node = result.group(1)
            a = result.group(2)
            b = result.group(3)
            network[node] = [a,b]
        i = i + 1

part1 = False
if part1:
    dest = "AAA"
    i = 0
    while dest != "ZZZ":
        idx = i if len(directions) > i else i % len(directions)
        dir = directions[idx]
        dir = 0 if dir == "L" else 1
        dest = network[dest][dir]
        i = i + 1

    print(f"Part 1: {i} steps")


start = []
ends = []
for k in network.keys():
    if k[2] == 'A':
        start.append(k)
    if k[2] == 'Z':
        ends.append(k)

print(f"start: {start}")
print(f"end: {ends}")

steps = []
for d in start:
    dest = d
    i = 0
    while dest[2] != 'Z':
        idx = i if len(directions) > i else i % len(directions)
        dir = directions[idx]
        dir = 0 if dir == "L" else 1
        dest = network[dest][dir]
        i = i + 1
    steps.append(i)

print(f"steps for each starting point: {steps}")
print(f"LCM for all steps is {math.lcm(*steps)}")


#print(f"Part 1: {i} steps")

