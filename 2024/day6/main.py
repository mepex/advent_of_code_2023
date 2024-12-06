from copy import deepcopy
from pprint import pprint

grid = []
start = (0,0)
f = 'input.txt'
with open(f) as fp:
    i = 0
    for line in fp:
        line = line.strip()
        grid.append(list(line))
        if "^" in line:
            start = (i, line.index('^'))
        i += 1

h = len(grid)
w = len(grid[0])

visited = deepcopy(grid)

def move(v, y, x, dir):
    global w, h
    next_dir = {'N': 'W', 'S': 'E', 'E':'N', 'W':'S'}
    next_y = y
    next_x = x
    v[y][x] = 'X'
    if dir == 'N':
        next_y -= 1
    elif dir == 'S':
        next_y += 1
    elif dir == "E":
        next_x -= 1
    elif dir == "W":
        next_x += 1
    if next_y < 0 or next_y == h or next_x < 0 or next_x == w:
        return True, 0, 0, 'N'
    if v[next_y][next_x] == '#':
        return False, y, x, next_dir[dir]
    return False, next_y, next_x, dir

done, y, x, dir = move(visited, start[0], start[1], 'N')

path_length = 1
while not done:
    done, y, x, dir = move(visited, y, x, dir)
    path_length += 1

pos_count = 0
for v in visited:
    pos_count += v.count('X')
    print(''.join(v))

print(f"part 1: {pos_count} length = {path_length}")

# max number of steps is the size of the grid, roughly
max = h * w
loops = 0
solutions = []

for i in range(h):
    for j in range(w):
        # if there's already an obstacle there or we never walk there, no need to check
        if visited[i][j] == '#' or visited[i][j] == '.':
            continue
        # also can't have the set obstacle right above starting point
        if (i == start[0] and j == start[1]) or (i == start[0]-1 and j == start[1]):
            continue
        # record each position and direction in the path, if it's ever repeated we have a loop
        t = 0
        visited[i][j] = '#'
        done, y, x, dir = move(visited, start[0], start[1], 'N')
        while t < h * w and not done:
            done, y, x, dir = move(visited, y, x, dir)
            t += 1
        if not done:
            loops += 1
            solutions.append((i, j))
        visited[i][j] = 'X'

print(solutions)
print(f"part 2: {loops}")





