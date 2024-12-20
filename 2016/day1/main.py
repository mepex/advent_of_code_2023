from mymodule import *

lines = get_lines('input.txt')

# x, y
pos = [0, 0]
current = 'N'
next_dir = {'NR' : 'E', "NL": "W", 'SR': 'W', 'SL': 'E', 'WR': 'N', 'WL': 'S', 'ER': 'S', 'EL': 'N'}

dirs = [x.strip() for x in lines[0].split(',')]

dir_m = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}

positions = [(0,0)]
for d in dirs:
    c = current
    p = pos
    current = next_dir[current + d[0]]
    dist = int(d[1:])
    #move = [dist * x for x in dir_m[current]]
    for i in range(dist):
        pos = [pos[0] + dir_m[current][0], pos[1] + dir_m[current][1]]
        if tuple(pos) in positions:
            print(f'part 2: {pos}, {abs(pos[0]) + abs(pos[1])}')
        else:
            positions.append(tuple(pos))
    print(f"{p} heading {c} : {d} -> {pos} going {current}")

print(f"part 1: {pos} {abs(pos[0]) + abs(pos[1])}")

