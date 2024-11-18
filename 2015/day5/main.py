import re

f = "input.txt"
count = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        x = re.findall("[aeiou]", line)
        y = re.search(r"(.)\1", line)
        z = re.findall("ab|cd|pq|xy", line)
        if len(x) > 2 and y and len(z) == 0:
            count += 1

print(f"part 1: {count}")

count = 0

with open(f) as fp:
    for line in fp:
        line = line.strip()
        x = re.search(r"(..).*\1", line)
        y = re.search(r"(.).\1", line)
        if x and y:
            count += 1

print(f"part 2: {count}")
