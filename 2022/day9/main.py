import numpy as np
import re
import copy

import pandas as pd
desired_width = 500
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

np.set_printoptions(threshold=np.inf)

positions = []

def next_t(ch, ct):
    if ch == ct:
        return ct.copy()
    x, y = ct[0], ct[1]
    dx = abs(ch[0] - ct[0])
    dy = abs(ch[1] - ct[1])
    if dx > 1:
        x = int((ch[0] + ct[0]) / 2)
        if dy == 1:
            y = ch[1]
    if dy > 1:
        y = int((ch[1] + ct[1]) / 2)
        if dx == 1:
            x = ch[0]
    return [x, y]


current_h = [0, 0]
current_t = [0, 0]
head_history = {}
tail_history = {}
with open("input.txt") as fp:
    for line in fp:
        match = re.match(r"(\w) (\d+)", line)
        if match:
            d = match.group(1)
            l = int(match.group(2))
            for i in range(l):
                if d == "D":
                    current_h = [current_h[0], current_h[1] - 1]
                if d == "U":
                    current_h = [current_h[0], current_h[1] + 1]
                if d == "L":
                    current_h = [current_h[0] - 1, current_h[1]]
                if d == "R":
                    current_h = [current_h[0] + 1, current_h[1]]
                current_t = next_t(current_h, current_t)
                print(f"{current_h} {current_t}")
                head_history[str(current_h)] = 1
                tail_history[str(current_t)] = 1
        else:
            exit(1)

print(head_history)
print(tail_history)
print(f"tail spaces: {len(tail_history.keys())}")

current_h = [0, 0]
knots = 10
current_knot = []
for i in range(knots):
    current_knot.append([0,0])
head_history = {}
tail_history = {}
with open("input.txt") as fp:
    for line in fp:
        match = re.match(r"(\w) (\d+)", line)
        if match:
            d = match.group(1)
            l = int(match.group(2))
            for i in range(l):
                if d == "D":
                    current_knot[0] = [current_knot[0][0], current_knot[0][1] - 1]
                if d == "U":
                    current_knot[0] = [current_knot[0][0], current_knot[0][1] + 1]
                if d == "L":
                    current_knot[0] = [current_knot[0][0] - 1, current_knot[0][1]]
                if d == "R":
                    current_knot[0] = [current_knot[0][0] + 1, current_knot[0][1]]
                for k in range(1,knots):
                    current_knot[k] = next_t(current_knot[k-1], current_knot[k])
                print(f"{current_knot}")
                head_history[str(current_knot[0])] = 1
                tail_history[str(current_knot[knots-1])] = 1
        else:
            exit(1)

print(head_history)
print(tail_history)
print(f"tail spaces: {len(tail_history.keys())}")
