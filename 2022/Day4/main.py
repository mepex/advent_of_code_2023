
full_overlap = 0
with open("input.txt") as fp:
    for line in fp:
        # replace , and - with spaces, get the four numbers out
        s = line.strip().replace('-', ' ').replace(',', ' ').split()
        ints = [int(x) for x in s]
        # second section range is to the left of the first
        if ints[2] >= ints[0] and ints[3] <= ints[1]:
            full_overlap = full_overlap + 1
        elif ints[0] >= ints[2] and ints[1] <= ints[3]:
            full_overlap = full_overlap + 1

print(f"part one: full_overlap is {full_overlap}")

full_overlap = 0
with open("input.txt") as fp:
    for line in fp:
        # replace , and - with spaces, get the four numbers out
        s = line.strip().replace('-', ' ').replace(',', ' ').split()
        ints = [int(x) for x in s]
        # if any of the end points are between the other pair, inclusive
        if ints[0] <= ints[2] <= ints[1]:
            full_overlap = full_overlap + 1
        elif ints[0] <= ints[3] <= ints[1]:
            full_overlap = full_overlap + 1
        elif ints[2] <= ints[0] <= ints[3]:
            full_overlap = full_overlap + 1
        elif ints[2] <= ints[1] <= ints[3]:
            full_overlap = full_overlap + 1
        else:
            print(f"Fail: {ints}")

print(f"part one: any_overlap is {full_overlap}")


