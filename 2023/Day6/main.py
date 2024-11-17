import re
import numpy

f = "input.txt"
times = []
distances = []

with open(f) as fp:
    for line in fp:
        result = re.search(r": (.*)", line.strip())
        if not times:
            times = result.group(1).split()
            times = list(map(lambda x: int(x), times))
        elif not distances:
            distances = result.group(1).split()
            distances = list(map(lambda x: int(x), distances))

all_wins = []
for i in range(len(times)):
    t = times[i]
    d = distances[i]
    wins = 0
    for j in range(1, t):
        # performace is the speed (j) times the number of ms (time left)
        p = j * (t-j)
        if p > d:
            wins = wins + 1
            print(f"  Win: speed = {j} dist = {p} beats {d}")
    print(f"Race {i} : {wins} wins")
    all_wins.append(wins)


print(f"Part 1 total product = {numpy.prod(all_wins)}")

time = 0
distance = 0
with open(f) as fp:
    for line in fp:
        result = re.search(r": (.*)", line.strip())
        if not time:
            times = result.group(1).split()
            time = int("".join(times))
        elif not distance:
            distances = result.group(1).split()
            distance = int("".join(distances))

wins = 0
for j in range(1, time):
    # performace is the speed (j) times the number of ms (time left)
    p = j * (time-j)
    if p > distance:
        wins = wins + 1
        # print(f"  Trial {j} of {time} wins: speed = {j} dist = {p} beats {distance}")
print(f"Part 2 : {wins} wins")
