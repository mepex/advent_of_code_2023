import math

f = "input.txt"
total = 0
with open(f) as fp:
    for line in fp:
      d = [int(x) for x in line.strip().split('x')]
      a = d[0] * d[1]
      b = d[0] * d[2]
      c = d[1] * d[2]
      smallest = min(a,b,c)
      area = 2 * a + 2 * b + 2 * c + smallest
      total += area

print(f"part 1: {total}")

total = 0
with open(f) as fp:
    for line in fp:
      d = [int(x) for x in line.strip().split('x')]
      d2 = sorted(d)
      ribbon = d2[0] * 2 + d2[1] * 2
      vol = math.prod(d2)
      total += ribbon + vol

print(f"part 2: {total}")
