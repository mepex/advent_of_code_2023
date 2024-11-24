import json
import re

#parse x
# y = json.loads(x)



def find_nums(d):
    total = 0
    if isinstance(d, list):
        for e in d:
            total += find_nums(e)
    elif isinstance(d, dict):
        if 'red' in d.values():
            return 0
        for k in d.keys():
            total += find_nums(d[k])
    elif isinstance(d, str):
        try:
            total = int(d)
        except ValueError as ve:
            total = 0
    elif isinstance(d, int):
        total = d
    return total

# don't even need to parse the json, just look for the numbers
with open('input.txt', 'r') as file:
    data = file.read()

s = re.findall('[+-]?\d+', data)
total = 0
for i in s:
    total += int(i)

print(f"part1: {total}")

print(find_nums(json.loads(data)))