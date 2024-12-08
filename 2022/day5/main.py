import re
import copy

# create 2D array of chars for initial condition

pixels = []
with open("input.txt") as fp:
    for line in fp:
        if not line.strip().startswith("move"):
            pixels.append(list(line))


# empty line
pixels.pop()
# numbers
pixels.pop()
num_bins = int((len(pixels[0]) + 1)/4)
stack = []
for i in range(num_bins):
    stack.append([])

for i in range(len(pixels)):
    v = pixels.pop()
    for j in range(num_bins):
        crate = v[j*4 + 1]
        if crate != ' ':
            stack[j].append(crate)

#stacks are ZERO INDEXED
print(stack)

part2 = copy.deepcopy(stack)

with open("input.txt") as fp:
    for line in fp:
        if line.startswith('move'):
            m = re.search(r"move (\d+) from (\d+) to (\d+)", line.strip())
            if m:
                amount = int(m.group(1))
                source = int(m.group(2)) - 1
                dest = int(m.group(3)) - 1
            else:
                assert f"no match! {line}"

            for i in range(amount):
                crate = stack[source].pop()
                stack[dest].append(crate)

final = ""
for j in range(num_bins):
    final += stack[j].pop()

print(f"part one answer: {final}")

with open("input.txt") as fp:
    for line in fp:
        if line.startswith('move'):
            m = re.search(r"move (\d+) from (\d+) to (\d+)", line.strip())
            if m:
                amount = int(m.group(1))
                source = int(m.group(2)) - 1
                dest = int(m.group(3)) - 1
            else:
                assert f"no match! {line}"

            crates = []
            for i in range(amount):
                crates.insert(0, part2[source].pop())

            part2[dest] += crates

final = ""
for j in range(num_bins):
    final += part2[j].pop()

print(f"part two answer: {final}")

