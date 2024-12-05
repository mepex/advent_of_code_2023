import re

f = 'input.txt'
rules = []
updates = []
with open(f) as fp:
    for line in fp:
        line = line.strip()
        m = re.search(r'(\d+)\|(\d+)', line)
        if m:
          rules.append((int(m.group(1)), int(m.group(2))))
        m = re.search(r',', line)
        if m:
            updates.append([int(x) for x in line.split(',')])

def find_page(rules, page):
    r = []
    for rule in rules:
        if rule[0] == page or rule[1] == page:
            r.append(rule)
    return r

class IncorrectOrder(Exception):
    pass

correct = []
incorrect = []
for u in updates:
    try:
        for p in u:
            r = find_page(rules, p)
            for rule in r:
                if rule[0] not in u or rule[1] not in u:
                    pass
                elif p == rule[0] and u.index(rule[1]) > u.index(p):
                    pass
                elif p == rule[1] and u.index(rule[0]) < u.index(p):
                    pass
                else:
                    raise IncorrectOrder
    except IncorrectOrder:
        incorrect.append(u)
        continue
    correct.append(u)

middle_sum = 0
for c in correct:
    middle_sum += c[len(c)//2]

print(f"part 1: {middle_sum}")

for c in incorrect:
    i = 0
    while i < len(c):
        p = c[i]
        r = find_page(rules, p)
        swap = False
        for rule in r:
            a = rule[0]
            b = rule[1]
            # if rule is incorrect, just swap the places of the pages in the rule
            if a not in c or b not in c:
                continue
            a_pos = c.index(a)
            b_pos = c.index(b)
            if p == rule[0] and a_pos > b_pos:
                c[b_pos] = p
                c[a_pos] = b
                swap = True
            elif p == rule[1] and a_pos > b_pos:
                c[a_pos] = p
                c[b_pos] = a
                swap = True
        # start over at the beginning and check all the rules again if we messed with the page order
        if swap:
            i = 0
        else:
            i += 1

middle_sum = 0
for c in incorrect:
    middle_sum += c[len(c)//2]

print(f"part 2: {middle_sum}")



