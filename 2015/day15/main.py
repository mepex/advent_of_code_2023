import re
import math
import itertools

f = "input.txt"
ingred = {}
with open(f) as fp:
    for line in fp:
        m = re.search(r'(\w+): capacity ([+-]?\d+), durability ([+-]?\d+), flavor ([+-]?\d+), texture ([+-]?\d+), calories ([+-]?\d+)', line)
        if m:
            n = m.group(1)
            ingred[n] = [int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6))]


def get_score1(ingred, amounts):
    scores = []
    for i in range(4):
        idx = 0
        s = 0
        for k, v in ingred.items():
            s += amounts[idx] * v[i]
            idx += 1
        if s <= 0:
            return 0
        scores.append(s)
    return math.prod(scores)





num_ingred = len(ingred.keys())

start = 100 // num_ingred
amounts = [start] * num_ingred
if sum(amounts) != 100:
    amounts[-1] = 100 - sum(amounts[:-1])

done = False
s = 0
last_s = 0
idx = 0


def partitions(n, k):
    """
    :param n: number of items
    :param k: number of buckets
    :return: array of all possible partitions of n in k buckets where 0 is allowed
    """
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]


scores = []
for p in partitions(100, num_ingred):
    s = get_score1(ingred, p)
    scores.append(s)
    print(f"{p} : {s}")

print(f"part 1 top score: {max(scores)}")

def get_score2(ingred, amounts):
    scores = []
    idx = 0
    cals = 0
    for k, v in ingred.items():
        cals += amounts[idx] * v[4]
        idx += 1
    if cals != 500:
        return 0

    for i in range(4):
        idx = 0
        s = 0
        for k, v in ingred.items():
            s += amounts[idx] * v[i]
            idx += 1
        if s <= 0:
            return 0
        scores.append(s)
    return math.prod(scores)

scores = []
for p in partitions(100, num_ingred):
    s = get_score2(ingred, p)
    scores.append(s)
    print(f"{p} : {s}")

print(f"part 2 top score: {max(scores)}")



