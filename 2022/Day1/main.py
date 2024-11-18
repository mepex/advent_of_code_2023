count = 0
elves = []
cals = 0
with open("input.txt") as fp:
    for line in fp:
        count += 1
        if line.strip() != "":
            cals = cals + int(line.strip())
        else:
            elves.append(cals)
            cals = 0

elves.sort()
print(f"Part one: Max cals is {elves[-1]}")

top = elves[-1]
second = elves[-2]
third = elves[-3]
top3 = top + second + third

print(f"part two: top 3 total cals is {top3}")
