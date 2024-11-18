
#use ASCII table to get numbers, and offset to get priority
def get_priority(c):
    offset_upper = ord('A') - 27
    offset_lower = ord('a') - 1
    if c.isupper():
        return ord(c) - offset_upper
    else:
        return ord(c) - offset_lower


assert get_priority('a') == 1
assert get_priority('z') == 26
assert get_priority('A') == 27
assert get_priority('Z') == 52

priority_sum = 0
with open("input.txt") as fp:
    for line in fp:
        sack = line.strip()
        midpoint = int(len(sack)/2)
        c1 = sack[:midpoint]
        c2 = sack[midpoint:]
        for c in c1:
            if c2.find(c) != -1:
                current_priority = get_priority(c)
                priority_sum = priority_sum + current_priority
                break

print(f"Part one answer: {priority_sum}")

priority_sum = 0
with open('input.txt') as f:
    lines = [line.rstrip() for line in f]
    for i in range(0, len(lines), 3):
        l1 = lines[i]
        l2 = lines[i + 1]
        l3 = lines[i + 2]
        for c in l1:
            if l2.find(c) != -1 and l3.find(c) != -1:
                current_priority = get_priority(c)
                priority_sum = priority_sum + current_priority
                break

print(f"Part two answer: {priority_sum}")
