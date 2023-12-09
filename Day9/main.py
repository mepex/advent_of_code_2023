import re
import numpy
import math

f = "input.txt"

def go_down(current_line):
    sequence_below = []
    if len(set(current_line)) == 1:
        # all elements have the same value
        return [0] * (len(current_line) - 1)

    for ind in range(len(current_line) - 1):
        sequence_below.append(current_line[ind + 1] - current_line[ind])
    return sequence_below


def go_up(sequences):
    for ind in range(len(sequences) - 1, 0, -1):
        last_el_last_line = sequences[ind][-1]
        last_el_line_above = sequences[ind - 1][-1]
        sequences[ind - 1].append(last_el_last_line + last_el_line_above)
    return sequences[0][-1]


def extrapolate_history(line):
    current_line = list(map(int, line.split()))
    is_all_zero = False
    sequences = [current_line]

    # go down
    while not is_all_zero:
        line_below = go_down(current_line)
        sequences.append(line_below)
        is_all_zero = all([x == 0 for x in line_below])
        current_line = line_below

    # go up
    r = go_up(sequences)
    for s in sequences:
        print(s)
    return r

total = 0
with open(f) as fp:
    i = 0
    for line in fp:
        diffs = []
        line = line.strip()
        result = re.findall(r"[0-9-]+", line)
        a = [int(x) for x in result]
        done = False
        n = a.copy()
        while not done:
            d = []
            for i in range(len(n) - 1):
                d.append(n[i+1] - n[i])
            if d.count(0) == len(d):
                done = True
                d.append(0)
            diffs.append(d)
            n = d.copy()
        i = 0
        for i in range(len(diffs) - 2, -1, -1):
            prev = diffs[i+1]
            prev_last = prev[len(prev) - 1]
            last = diffs[i][len(diffs[i]) - 1]
            diffs[i].append(last + prev_last)
            i = i + 1
        new = (diffs[0][-1] + a[-1])
        total = total + new
        print(f"nums: \n{a}, new = {new}")
        gap = ""
        for d in diffs:
            gap = gap + (len(str(n)) * " ")
            print(f"{gap}", end = "")
            for n in d:
              print(f"{n} ", end = "")
            print("")
        print(f"total = {total}")
        if new != extrapolate_history(line):
            print(f"BAD:  should be {extrapolate_history(line)} not {new}")
            exit(-1)


print(f"Part 1 total: {total}")

total = 0
with open(f) as fp:
    i = 0
    for line in fp:
        diffs = []
        line = line.strip()
        result = re.findall(r"[0-9-]+", line)
        a = [int(x) for x in result]
        a.reverse()
        done = False
        n = a.copy()
        while not done:
            d = []
            for i in range(len(n) - 1):
                d.append(n[i+1] - n[i])
            if d.count(0) == len(d):
                done = True
                d.append(0)
            diffs.append(d)
            n = d.copy()
        i = 0
        for i in range(len(diffs) - 2, -1, -1):
            prev = diffs[i+1]
            prev_last = prev[len(prev) - 1]
            last = diffs[i][len(diffs[i]) - 1]
            diffs[i].append(last + prev_last)
            i = i + 1
        new = (diffs[0][-1] + a[-1])
        total = total + new
        print(f"nums: \n{a}, new = {new}")
        gap = ""
        for d in diffs:
            gap = gap + (len(str(n)) * " ")
            print(f"{gap}", end = "")
            for n in d:
              print(f"{n} ", end = "")
            print("")
        print(f"total = {total}")


