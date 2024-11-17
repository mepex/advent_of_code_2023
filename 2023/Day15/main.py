import re
import numpy as np
import math
from functools import cache
from time import time


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


f = "input.txt"
grid = []

s = 0

def hash_tok(tok):
    cv = 0
    for ch in tok:
        cv = ((cv + ord(ch)) * 17) % 256
    return cv

def hash_line(toks):
    tot = 0
    for tok in toks:
        tot += hash_tok(tok)
    return tot

def remove_lens(boxes, boxnum, label):
    if boxes[boxnum]:
        for b in boxes[boxnum]:
            if b[0] == label:
                boxes[boxnum].remove(b)

def add_lens(boxes, boxnum, label, fl):
    if not boxes[boxnum]:
        boxes[boxnum] = [[label, fl]]
        return boxes
    else:
        for i in range(len(boxes[boxnum])):
            if boxes[boxnum][i][0] == label:
                boxes[boxnum][i][1] = fl
                return boxes
        boxes[boxnum].append([label, fl])
        return boxes


def print_boxes(boxes):
    for i in range(len(boxes)):
        if boxes[i]:
            print(f"{i} : {boxes[i]}")
    print("---")

def focusing_power(boxes):
    p = 0
    for i in range(len(boxes)):
        slot = 0
        if boxes[i]:
            for b in boxes[i]:
                power = (i+1) * (slot+1) * (int(b[1]))
                p += power
                slot += 1
    return p

def part2_hash_line(toks):
    boxes = [None] * 256
    for t in toks:
        labels = re.split(r"[-=]", t)
        boxnum = hash_tok(labels[0])
        if t.find('-') >= 0:
            # remove lens
            h = hash_tok(labels[0])
            remove_lens(boxes, boxnum, labels[0])
        elif t.find('=') >= 0:
            # add lens
            boxes = add_lens(boxes, boxnum, labels[0], labels[1])
        else:
            print(f"ERROR, no - or = : {t}")
        #print_boxes(boxes)
    return focusing_power(boxes)



with open(f) as fp:
    for line in fp:
        line = line.strip()
        if line != '':
            hash = hash_line(line.split(','))
            print(f"Part 1: {hash}")
            print(f"Part 2: {part2_hash_line(line.split(','))}")




