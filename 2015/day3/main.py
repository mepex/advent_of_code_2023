from collections import Counter

f = "input.txt"
with open(f) as fp:
    for line in fp:
        line = line.strip()

houses = [(0,0)]
position = (0,0)
for ch in line:
    if ch == '>':
        position = (position[0] + 1, position[1])
    if ch == '<':
        position = (position[0] - 1, position[1])
    if ch == '^':
        position = (position[0], position[1] + 1)
    if ch == 'v':
        position = (position[0], position[1] - 1)
    houses.append(position)

c = Counter(houses)
print(f"part 1: num of houses : {len(c.keys())}")

#stuff goes here

houses = [(0,0)]
s_pos = (0,0)
r_pos = (0,0)
i = 0
for ch in line:
    if i % 2:
        position = s_pos
    else:
        position = r_pos
    if ch == '>':
        position = (position[0] + 1, position[1])
    if ch == '<':
        position = (position[0] - 1, position[1])
    if ch == '^':
        position = (position[0], position[1] + 1)
    if ch == 'v':
        position = (position[0], position[1] - 1)
    if i % 2:
        s_pos = position
    else:
        r_pos = position
    houses.append(position)
    i += 1

c = Counter(houses)
print(f"part 2: num of houses : {len(c.keys())}")

