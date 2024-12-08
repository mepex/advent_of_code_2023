import re
from itertools import combinations

f = 'input.txt'
eqs = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.findall(r'(\d+)', line)
        eqs.append([int(x) for x in m])

def iterate_actions(pos):
    actions[pos] = '*+'['+*'.index(actions[pos])]
    if actions[pos] == '+':
        if pos + 1 < len(actions):
            iterate_actions(pos+1)

def iterate_actions2(pos):
    global actions
    actions[pos] = '*|+'['+*|'.index(actions[pos])]
    if actions[pos] == '+':
        if pos + 1 < len(actions):
            iterate_actions2(pos+1)

def test_eq(a, b, ops):
    local_ops = ops.copy()
    for i in range(len(ops)):
        if local_ops[i] == "|":
            local_ops[i] = ''

    result = eval(f"{b[0]}{local_ops[0]}{b[1]}")
    for n in range(1, len(ops)):
        result = eval(f"{result}{local_ops[n]}{b[n+1]}")
        if result > a:
            return False
    if a == result:
        return True
    return False

def get_eq(a, b, ops):

    r = f"{a} = {b[0]} {ops[0]} {b[1]}"
    for n in range(1, len(ops)):
        r += f" {ops[n]} {b[n + 1]}"
    return r


good = []
for eq in eqs:
    a = eq[0]
    num_ops = len(eq[1:])-1
    actions = ['+'] * (len(eq[1:])-1)
    for i in range(2**num_ops):
        correct = test_eq(a, eq[1:], actions)
        if correct:
            good.append(a)
            print(f"good: {get_eq(a, eq[1:], actions)}")
            break
        iterate_actions(0)

print(f"part 1: {sum(good)}")

good = []
for eq in eqs:
    a = eq[0]
    num_ops = len(eq[1:])-1
    actions = ['+'] * (len(eq[1:])-1)
    for i in range(3**num_ops):
        correct = test_eq(a, eq[1:], actions)
        if correct:
            good.append(a)
            print(f"good: {get_eq(a, eq[1:], actions)}")
            break
        iterate_actions2(0)

print(f"part 2: {sum(good)}")




