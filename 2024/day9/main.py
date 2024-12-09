from mymodule import *

lines = get_lines("input.txt")

mymap = list(lines[0])

blocks = [int(x) for x in mymap]
disk = []

for i in range(len(blocks)):
    if i % 2:

        disk.extend([-1] * blocks[i])
    else:
        b = i // 2
        disk.extend([b] * blocks[i])

gold_disk = disk.copy()

print(f"Found {i//2} files")
def get_element(d, e):
    try:
        return d.index(e)
    except ValueError:
        return -1

e = get_element(disk, -1)
while e != -1:
    b = disk.pop(-1)
    while b == -1:
        b = disk.pop(-1)
    try:
        disk[e] = b
    except IndexError:
        disk.append(b)
    e = get_element(disk, -1)

checksum = 0
for i in range(len(disk)):
    if disk[i] != -1:
        checksum += i * disk[i]

print(f"part 1: {checksum}")

def map_blanks(fs):
    blank_map = []
    size = 0
    start = 0
    for i in range(len(fs)):
        if fs[i] == -1:
            if size == 0:
                start = i
            size += 1
        else:
            if size > 0:
                blank_map.append((start, size))
            size = 0
    return blank_map

file_map = []
size = 0
start = 0
idx = -1
for i in range(len(gold_disk)):
    if gold_disk[i] != -1:
        if gold_disk[i] != idx:
            if size > 0:
                file_map.append((start, size))
            idx = gold_disk[i]
            size = 0
            start = i
        size += 1
    else:
        if size > 0:
            file_map.append((start, size))
        size = 0
if size > 0:
    file_map.append((start, size))


disk = gold_disk.copy()

blank_map = map_blanks(disk)
for i in range(len(file_map)-1 , -1, -1):
    f = file_map[i]
    for j in range(len(blank_map)):
        b = blank_map[j]
        if b[1] >= f[1] and b[0] < f[0]:
            for j in range(f[1]):
                disk[b[0] + j] = i
                disk[f[0] + j] = -1
            blank_map = map_blanks(disk)
            break

checksum = 0
for i in range(len(disk)):
    if disk[i] != -1:
        checksum += i * disk[i]

print(f"part 2: {checksum}")





