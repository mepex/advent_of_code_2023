import re
import numpy as np
import math
from functools import cache
from time import time
import sys
from rule import Rule, Rules


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func



sys.setrecursionlimit(1000000)
f = "testinput.txt"
grid = []

inst = []
ruledef = True

rules = Rules()
total = 0
with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line == '':
            ruledef = False
            continue
        if ruledef:
            rules.add_rule(line)
        else:
            total += rules.run(line)

print(f"Part 1: {total}")

n = rules.build_root()
print(n)
print(rules.build_paths())
#rules.brute_force_segments()

