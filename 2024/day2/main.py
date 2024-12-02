import re

f = ("input.txt")
safe = 0
data = []

def is_safe(a):
    if a != sorted(a) and a != sorted(a, reverse=True):
        return False
    for i in range(1, len(a)):
        if abs(a[i] - a[i - 1]) > 3 or a[i] == a[i - 1]:
            return False
    return True

with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = [int(x) for x in re.findall(r'\d+', line)]
        data.append(m)
        if is_safe(m):
            safe += 1


print(f"part 1: {safe}")

safe = 0
for l in data:
    if not is_safe(l):
        for i in range(len(l)):
            if is_safe(l[:i] + l[i+1:]):
                safe += 1
                break
    else:
        safe += 1

print(f"part 2: {safe}")







