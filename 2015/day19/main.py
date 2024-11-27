import re
from collections import OrderedDict

f = "input.txt"
machine = []
base = ''
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.match(r'(\w+) => (\w+)', line)
        if m:
            machine.append((m.group(1), m.group(2)))
        elif line != '':
            base = str(line)


def replace_nth(sub, repl, txt, nth):
    arr = txt.split(sub)
    part1 = sub.join(arr[:nth])
    part2 = sub.join(arr[nth:])
    return part1 + repl + part2

derived = []
for m in machine:
    s = re.findall(m[0], base)
    for i in range(len(s)):
        derived.append(replace_nth(m[0], m[1], base, i+1))

distinct = set(derived)
print(f"part 1: {len(distinct)}")


print(replace_nth("H", "OH", "HH", 0))
print(replace_nth("H", "OH", "HH", 1))
print(replace_nth("H", "OH", "HH", 2))

sm = sorted(machine, key=lambda tup: len(tup[1]), reverse=True)
print(machine)
print(sm)

print(m)

m = re.findall(f'([A-Z][a-z])', base)
elements = list(m)

#
#  CHEAT:  used https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/
#
print(f"two letter elements: {len(m)} + ")
elements = len(base) - 2*len(m)
print(f"single letter elements {elements}")
total_elements = elements + 2*len(m)

m = re.findall(r'(Rn|Ar)', base)
brackets = len(m)
print(f"there are {brackets} Rn or Ars")
m = re.findall(r'Y', base)
commas = len(m)
print(f"there are {commas} Ys")

answer = total_elements - brackets - (2*commas)
print(answer)




