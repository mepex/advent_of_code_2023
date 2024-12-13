from mymodule import *
import re
import math

list_a = []
list_b = []
list_prize = []
lines = get_lines('input.txt')

for l in lines:
    m = re.search(r'Button ([AB]): X\+(\d+), Y\+(\d+)', l)
    if m:
        if m.group(1) == 'A':
            list_a.append((int(m.group(2)), int(m.group(3))))
        elif m.group(1 == 'B'):
            list_b.append((int(m.group(2)), int(m.group(3))))
    m = re.search(r'Prize: X=(\d+), Y=(\d+)', l)
    if m:
        list_prize.append((int(m.group(1)), int(m.group(2))))

def solve(list_a, list_b, list_prize):
    soln = []
    tokens = 0
    while len(list_a):
        a = list_a.pop(0)
        b = list_b.pop(0)
        prize = list_prize.pop(0)
        asolve = math.lcm(a[0], a[1])
        multa = asolve // a[0]
        multb = asolve // a[1]
        print(f"asolve is {asolve} {multa} {multb}")
        bsoln = (prize[0] * multa - prize[1] * multb) / (b[0] * multa - b[1] * multb)
        if bsoln.is_integer():
            bsoln = int(bsoln)
            asoln = (prize[0] - bsoln * b[0]) // a[0]
            print(f"{asoln} {bsoln}")
            soln.append((asoln, bsoln))
            tokens += (asoln * 3) + bsoln
        print()
    return tokens

extra = 10000000000000
list_prize_2 = [(x[0] + extra, x[1] + extra) for x in list_prize]
list_a_2 = list_a.copy()
list_b_2 = list_b.copy()
tokens = solve(list_a, list_b, list_prize)
print(f"part 1: {tokens}")


tokens = solve(list_a_2, list_b_2, list_prize_2)
print(f"part 2: {tokens}")


