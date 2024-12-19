from mymodule import *
from functools import cache

lines = get_lines('input.txt')
patterns = [x.strip() for x in lines[0].split(',')]

designs = lines[2:].copy()
@cache
def get_patterns(start, max):
    global patterns
    """
    Get all patterns that start with given string, sorted with longest pattern first
    :param patterns:
    :param start:
    :param max max pattern size
    :return:
    """
    x = [x for x in patterns if x.startswith(start) and len(x) <= max]
    x.sort(key=len)
    x.reverse()
    return x
@cache
def has_comb(design):
    global patterns
    pats = get_patterns(design[0], len(design))
    match = 0
    for p in pats:
        if design.startswith(p):
            if len(p) == len(design):
                match += 1
            else:
                match += has_comb(design[len(p):])
    return match

count = 0
total = 0
for d in designs:
    matches = has_comb(d)
    if matches:
        count += 1
    total += matches
    print(f"{d} : {matches}")

print(f"part 1: {count}")
print(f"part 2: {total}")