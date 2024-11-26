from itertools import combinations

f = "input.txt"
weights = {}
count = 0
sizes = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        sizes.append(int(line))

total = 150

solutions = 1 if total in sizes else 0
# cut down combinations, if smallest combination of sizes is bigger than total, we don't need to go through
# those combinations
top = 2
print(sorted(sizes))
s = sum(sorted(sizes)[:top])
while top < len(sizes) and sum(sorted(sizes)[:top]) < total:
    top += 1

answers = []
for i in range(2, top):
    c = combinations(sizes, i)
    for comb in c:
        if sum(comb) == total:
            solutions += 1
            answers.append(comb)

print(f"part 1 solutions: {solutions}")

num_sols = [0] * top
for a in answers:
    num_sols[len(a)] += 1

print(f"number of solutions per combination size: {num_sols}")