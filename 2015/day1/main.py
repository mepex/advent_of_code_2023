
sample = ")())())"
floor = 0
f = "input.txt"
with open(f) as fp:
    for line in fp:
        s = line.strip()

for ch in s:
    if ch == '(':
        floor += 1
    if ch == ')':
        floor -= 1
print(floor)

#part 2
floor = 0
i = 1
for ch in s:
    if ch == '(':
        floor += 1
    if ch == ')':
        floor -= 1
    if floor < 0:
        print(f"position {i}")
        break
    i += 1