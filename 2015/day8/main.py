import re

f = "input.txt"

with open(f) as fp:
    strings = fp.readlines()

def to_raw(st):
    return fr"{st}"

code = []
ch = []
count = 0
i = 0
for s in strings:
    s = s.strip()
    r = to_raw(s.strip())
    code.append(len(r))
    a = len(s)
    b = len(eval(s))
    print(f"{i}: {s} : {a} and {b}")
    count += a - b
    i += 1

print(count)

#cheating!!!
print(sum(len(s) - len(eval(s)) for s in open('input.txt')))
print(sum(2+s.count('\\')+s.count('"') for s in open('input.txt')))

