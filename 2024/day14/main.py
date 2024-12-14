import math

from matplotlib.animation import FuncAnimation

from mymodule import *
import numpy as np
import re
from copy import deepcopy
from time import sleep
import random
from operator import add
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

lines = get_lines('input.txt')
robots = []
speeds = []
for l in lines:
    m = re.search(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', l)
    if m:
        robots.append([int(m.group(1)), int(m.group(2))])
        speeds.append([int(m.group(3)), int(m.group(4))])

robot_start = deepcopy(robots)
print(robots)

size = (11, 7)

size = (101, 103)



def get_grid(size, robots, show = False):
    grid = []
    for j in range(size[1]):
        grid.append([])
        for i in range(size[0]):
            if [i, j] in robots:
                grid[j].append('1')
                if show:
                    print(robots.count([i, j]), end='')
            else:
                grid[j].append('0')
                if show:
                    print('.', end='')
        if show:
            print()
    if show:
        print()
    return grid

def get_grid2(size, robots):
    grid = []
    for i in range(size[1]):
        grid.append([0] * size[0])
    for r in robots:
        grid[r[1]][r[0]] = 1
    return grid


time = 100
for r in range(len(robots)):
    px, py = robots[r]
    vx, vy = speeds[r]
    px = (px + time*vx) % size[0]
    py = (py + time*vy) % size[1]
    robots[r] = [px, py]

get_grid(size, robots, True)

print(robots)

quadrants = [0,0,0,0]
for r in robots:
    x, y = r
    if x < size[0] // 2 and y < size[1] // 2:
        quadrants[0] += 1
        print(f"{r} -> 0")
    elif x > size[0] // 2 and y < size[1] // 2:
        quadrants[1] += 1
        print(f"{r} -> 1")
    elif x < size[0] // 2 and y > size[1] // 2:
        quadrants[2] += 1
        print(f"{r} -> 2")
    elif x > size[0] // 2 and y > size[1] // 2:
        quadrants[3] += 1
        print(f"{r} -> 3")
    else:
        print(f"{r} -> none")

print(quadrants)

get_grid(size, robots, True)

print(f"part 1: {math.prod(quadrants)}")

def check_tree(size, robots):
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1,1], [-1, 1], [1, -1], [-1, -1]]
    for r in robots:
        c = 0
        for d in range(len(dirs)):
            n = list(map(add, r, dirs[d]))
            if n in robots:
                c += 1
            else:
                break
        if c == len(dirs):
            return True
    return False



def visualize(frames, vmax = 1):
    grid = np.zeros((103, 101), dtype = int)
    fig, ax = plt.subplots()
    im = ax.imshow(grid, interpolation='none', aspect='auto', vmin=0, vmax=vmax)

    def update(frame):
        #process_inst2(grid, instructions[frame])
        #im.set_data(grid)
        im.set_array(frames[frame])
        ax.set_title(f"Step {frame}")
        #print(f"{frame}\n{im.get_array()}\n")
        return [im]

    ani = FuncAnimation(fig, update, frames=range(len(frames) - 20, len(frames)), interval=200, repeat=False)
    plt.show()
    return ani




robots = deepcopy(robot_start)
t = 0
frames = []
while t < 11000:
    for r in range(len(robots)):
        vx, vy = speeds[r]
        px, py = robots[r]
        px = (px + vx) % size[0]
        py = (py + vy) % size[1]
        robots[r] = [px, py]
    frames.append(get_grid2(size, robots))
    t += 1
    if t == 100:
        get_grid(size, robots, True)
    if t % 100 == 0:
        print(t)
    if check_tree(size, robots):
        print(f"found cluster at {t}")
        break

visualize(frames)




