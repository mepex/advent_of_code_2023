from mymodule import *
from pprint import pprint
from operator import add
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
grid = get_grid_of_chars('input.txt')

dir_hash = {'<': [0, -1], '>': [0, 1], '^': [-1, 0], 'v': [1, 0]}
reverse_dir_hash = {'<': [0, 1], '>': [0, -1], '^': [1, 0], 'v': [-1, 0]}

dirs = ''
for j in range(len(grid) - 1, 0, -1):
    if grid[j].find('#') == -1:
        if grid[j] != '':
            dirs = grid[j] + dirs
        del grid[j]
    else:
        break

grid2 = deepcopy(grid)

num_boxes = 0
for j in range(len(grid)):
    boxes = [i for i, letter in enumerate(grid[j]) if letter == 'O']
    num_boxes += len(boxes)

print(f"number of boxes = {num_boxes}")


def find_robot(grid):
    for j in range(len(grid)):
        i = grid[j].find('@')
        if i != -1:
            return [j, i]


def push(grid, pos, direction):
    global dir_hash, reverse_dir_hash
    d = dir_hash[direction]
    next = list(map(add, pos, d))
    gridch = grid[next[0]][next[1]]
    if gridch == 'O':
        r = push(grid, next, direction)
        if r != pos:
            grid[r[0]] = replace_char_in_str(grid[r[0]], r[1], 'O')
            return pos
        else:
            # if we didn't successfully push boxes we gotta backtrack
            rd = reverse_dir_hash[direction]
            back = list(map(add, pos, rd))
            return back
    elif gridch == '#':
        # gotta go backwards if we run into the wall
        rd = reverse_dir_hash[direction]
        back = list(map(add, pos, rd))
        return back
    elif gridch == '.':
        grid[next[0]] = replace_char_in_str(grid[next[0]], next[1], 'O')
        grid[pos[0]] = replace_char_in_str(grid[pos[0]], pos[1], '.')
        return pos
    print(f"PUSHING ILLEGAL CHAR: {direction}")
    exit(1)


def move(grid, robot, direction):
    global dir_hash
    d = dir_hash[direction]
    next = list(map(add, robot, d))
    nextch = grid[next[0]][next[1]]
    if nextch == '.':
        grid[robot[0]] = replace_char_in_str(grid[robot[0]], robot[1], '.')
        grid[next[0]] = replace_char_in_str(grid[next[0]], next[1], '@')
        return next
    elif nextch == '#':
        return robot
    elif nextch == 'O':
        r = push(grid, next, direction)
        if r != robot:
            grid[robot[0]] = replace_char_in_str(grid[robot[0]], robot[1], '.')
            grid[r[0]] = replace_char_in_str(grid[r[0]], r[1], '@')
        return r

    print(f"ILLEGAL CHAR: {direction}")
    exit(1)


def compute_gps(grid):
    gps = 0
    for j in range(len(grid)):
        boxes = [i for i, letter in enumerate(grid[j]) if letter == 'O']
        for b in boxes:
            gps += 100 * j + b
    return gps


robot = find_robot(grid)
print("Start:")
pprint(grid)
print(dirs)
print(robot)

for c in dirs:
    robot = move(grid, robot, c)
    #print(f"Move {c}:")
    #pprint(grid)

print("End")
pprint(grid)

gps = compute_gps(grid)
print(f"part 1: {gps}\n")

for j in range(len(grid2)):
    l = list(grid2[j])
    for i in range(len(l)):
        if l[i] == '#':
            l[i] = "##"
        if l[i] == 'O':
            l[i] = "[]"
        if l[i] == ".":
            l[i] = ".."
        if l[i] == "@":
            l[i] = "@."
    grid2[j] = ''.join(l)

f = open('m_startgrid.txt', 'w')
for i in grid2:
    print(i, file=f)

pprint(grid2)


def push_lr(grid, pos, direction):
    global dir_hash, reverse_dir_hash
    d = dir_hash[direction]
    ch = grid[pos[0]][pos[1]]
    next = list(map(add, pos, d))
    gridch = grid[next[0]][next[1]]
    if gridch == '[' or gridch == ']':
        r = push_lr(grid, next, direction)
        if r != pos:
            grid[r[0]] = replace_char_in_str(grid[r[0]], r[1], ch)
            return pos
        else:
            # if we didn't successfully push boxes we gotta backtrack
            rd = reverse_dir_hash[direction]
            back = list(map(add, pos, rd))
            return back
    elif gridch == '#':
        # gotta go backwards if we run into the wall
        rd = reverse_dir_hash[direction]
        back = list(map(add, pos, rd))
        return back
    elif gridch == '.':
        grid[next[0]] = replace_char_in_str(grid[next[0]], next[1], ch)
        grid[pos[0]] = replace_char_in_str(grid[pos[0]], pos[1], '.')
        return pos
    print(f"PUSHING ILLEGAL CHAR: {direction}")
    exit(1)


def do_moves(grid, moves):
    for k, v in moves.items():
        m_ch = v
        n = k
        grid[n[0]] = replace_char_in_str(grid[n[0]], n[1], m_ch)


def move_box(grid, pos, direction):
    """
    Must be called on left hand bracket, will return True, list of boxes to move if allowed,
    False otherwise
    :param grid:
    :param pos:
    :param direction:
    :return:
    """
    y, x = pos

    if direction == '^':
        hole = grid[y - 1][x:x + 2]
    else:
        hole = grid[y + 1][x:x + 2]
    inc = -1 if direction == "^" else 1
    moves = [(y, x)]
    if '#' in hole:
        return False, []
    if hole == "[]":
        movable, m1 = move_box(grid, (y + inc, x), direction)
        return movable, moves + m1
    if hole == "][":
        movable1, m1 = move_box(grid, (y + inc, x - 1), direction)
        movable2, m2 = move_box(grid, (y + inc, x + 1), direction)
        if movable1 and movable2:
            return True, moves + m1 + m2
    if hole == "].":
        movable1, m1 = move_box(grid, (y + inc, x - 1), direction)
        if movable1:
            return True, moves + m1
    if hole == ".[":
        movable2, m2 = move_box(grid, (y + inc, x + 1), direction)
        if movable2:
            return True, moves + m2
    if hole == "..":
        return True, moves
    return False, []


def do_move_boxes(grid, boxes: list, direction):
    # gotta move boxes from the outside in!
    boxes = sorted(boxes)
    inc = -1 if direction == "^" else 1
    if inc == 1:
        boxes.reverse()
    for b in boxes:
        grid[b[0]] = replace_char_in_str(grid[b[0]], b[1], '.')
        grid[b[0]] = replace_char_in_str(grid[b[0]], b[1] + 1, '.')
        grid[b[0] + inc] = replace_char_in_str(grid[b[0] + inc], b[1], '[')
        grid[b[0] + inc] = replace_char_in_str(grid[b[0] + inc], b[1] + 1, ']')


def move2(grid, robot, direction):
    global dir_hash
    d = dir_hash[direction]
    next = list(map(add, robot, d))
    nextch = grid[next[0]][next[1]]
    if nextch == '.':
        grid[robot[0]] = replace_char_in_str(grid[robot[0]], robot[1], '.')
        grid[next[0]] = replace_char_in_str(grid[next[0]], next[1], '@')
        return next
    elif nextch == '#':
        return robot
    elif nextch == '[' or nextch == ']':
        if direction == '>' or direction == '<':
            r = push_lr(grid, next, direction)
            if r != robot:
                grid[robot[0]] = replace_char_in_str(grid[robot[0]], robot[1], '.')
                grid[r[0]] = replace_char_in_str(grid[r[0]], r[1], '@')
            return r
        else:
            inc = -1 if direction == "^" else 1
            if nextch == '[':
                movable, moves = move_box(grid, [robot[0] + inc, robot[1]], direction)
                if movable:
                    do_move_boxes(grid, moves, direction)
                    grid[robot[0]] = replace_char_in_str(grid[robot[0]], robot[1], '.')
                    grid[next[0]] = replace_char_in_str(grid[next[0]], next[1], '@')
                    return next
            else:
                movable, moves = move_box(grid, [robot[0] + inc, robot[1] - 1], direction)
                if movable:
                    do_move_boxes(grid, moves, direction)
                    grid[robot[0]] = replace_char_in_str(grid[robot[0]], robot[1], '.')
                    grid[next[0]] = replace_char_in_str(grid[next[0]], next[1], '@')
                    return next
            return robot

    print(f"ILLEGAL CHAR: {nextch} {robot} {direction}")
    return [-1, -1]


def find_robots(grid):
    cnt = 0
    for j in range(len(grid)):
        i = grid[j].find('@')
        if i != -1:
            cnt += 1
    return cnt


def grid_valid(grid, num_boxes, robot, r, c):
    count_l = 0
    count_r = 0
    if robot[0] != r[0] and robot[1] != r[1]:
        print("bad robot motion!")
        return False
    for j in range(len(grid)):
        boxes = [i for i, letter in enumerate(grid[j]) if letter == '[']
        count_l += len(boxes)
        for b in boxes:
            if grid[j][b + 1] != ']':
                return False
        boxes = [i for i, letter in enumerate(grid[j]) if letter == ']']
        count_r += len(boxes)
    if count_l == count_r == num_boxes:
        return True
    return False


def compute_gps2(grid):
    gps = 0
    for j in range(len(grid)):
        boxes = [i for i, letter in enumerate(grid[j]) if letter == '[']
        for b in boxes:
            gps += 100 * j + b
    return gps


robot = find_robot(grid2)
print(robot)

moves = len(dirs)

frames = []

idx = 0
f = open('mylog.log', 'w')
for c in dirs:
    r = move2(grid2, robot, c)
    if r == [-1, -1]:
        print(f'BIG ERROR at {idx}')
        exit(1)

    if not grid_valid(grid2, num_boxes, robot, r, c):
        print(f"Move {idx}/{moves}: {c}:")
        pprint(grid2)
        print(f"boxes fucked at {idx} {r} {c}")
        print("Previous frame:")
        pprint(frames[idx - 1])
        print("ERROR!")
        exit(1)
    #print(f"Move {idx} {c}")
    robot = r
    #pprint(grid2)
    frames.append(deepcopy(grid2))
    if find_robots(grid2) > 1:
        print(f"BREAK on MOVE {idx}")
        break
    #print(calculate_gps_sum(grid2), file=f)
    idx += 1

print(idx)

pprint(grid2)

print(f"part 2: {compute_gps2(grid2)}")


def visualize(frames, vmax=1):
    grid = np.zeros((len(frames[0]), len(frames[0][0])), dtype=int)
    fig, ax = plt.subplots()
    im = ax.imshow(grid, interpolation='none', aspect='auto', vmin=0, vmax=vmax)

    def update(frame):
        #process_inst2(grid, instructions[frame])
        #im.set_data(grid)
        num_array = np.array([[ord(char) for char in row] for row in frames[frame]])
        im.set_array(num_array)
        ax.set_title(f"Step {frame}")
        return [im]

    ani = FuncAnimation(fig, update, frames=range(len(frames)), interval=200, repeat=False)
    plt.show()
    return ani

#visualize(frames, 100)
