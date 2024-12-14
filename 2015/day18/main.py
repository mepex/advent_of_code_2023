from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Function to replace values
def replace(x):
    if x == '#':
        return 1
    elif x == ".":
        return 0


f = "input.txt"
initial = []
with open(f) as fp:
    for line in fp:
        line = list(line.strip())
        initial.append(list(map(replace, line)))

pprint(initial)
size = len(initial)
i_np = np.array(initial)

frame_size = 101

now = np.zeros((size+2, size+2), dtype=int)
now[1:size+1, 1:size+1] = i_np

frames = np.zeros((frame_size, size+2, size+2), dtype = int)
frames[0] = now.copy()

print(now)
print(i_np)

def get_neighbor_total(state, x, y):

    #  shift to account for the zero padding around the outside
    i = x + 1
    j = y + 1
    if i == 0 or j == 0:
        return -1
    over = sum(state[j-1][i-1:i+2])
    same = state[j][i-1] + state[j][i+1]
    under = sum(state[j+1][i-1:i+2])
    return over + same + under


def visualize_lights(frames, vmax = 1):
    grid = np.zeros((size, size), dtype = int)
    fig, ax = plt.subplots()
    im = ax.imshow(grid, interpolation='none', aspect='auto', vmin=0, vmax=vmax)

    def update(frame):
        #process_inst2(grid, instructions[frame])
        #im.set_data(grid)
        im.set_array(frames[frame])
        ax.set_title(f"Step {frame}")
        #print(f"{frame}\n{im.get_array()}\n")
        return [im]

    ani = FuncAnimation(fig, update, frames=range(len(frames)), interval=20, repeat=False)
    plt.show()
    return ani

print("after 0 steps")
print(frames[0])
for now in range(1, frame_size):
    for y in range(0, size):
        for x in range(0, size):
            c = frames[now-1][y+1][x+1]
            n = get_neighbor_total(frames[now-1], x, y)
            #print(f"{x},{y} : {n}")
            # Plus 1 because we are working on the buffered version
            if c:
                frames[now][y+1][x+1] = 1 if n == 2 or n == 3 else 0
            else:
                frames[now][y+1][x+1] = 1 if n == 3 else 0
    #print(f"after {now} steps")
    #print(frames[now])

print(f"part 1 answer: {np.sum(frames[frame_size-1])}")

def is_corner(x,y, size):
    if x == y == 0 or x == y == size-1:
        return True
    if x == 0 and y == size-1:
        return True
    if x == size-1 and y == 0:
        return True
    return False

def get_neighbor_total2(state, x, y):

    #  shift to account for the zero padding around the outside
    i = x + 1
    j = y + 1
    if i == 0 or j == 0:
        return -1
    over = sum(state[j-1][i-1:i+2])
    same = state[j][i-1] + state[j][i+1]
    under = sum(state[j+1][i-1:i+2])
    return over + same + under

# put 1s in corners
frames[0][1][1] = 1
frames[0][size][size] = 1
frames[0][1][size] = 1
frames[0][size][1] = 1

print("after 0 steps")
print(frames[0])
for now in range(1, frame_size):
    for y in range(0, size):
        for x in range(0, size):
            c = frames[now-1][y+1][x+1]
            n = get_neighbor_total2(frames[now-1], x, y)
            #print(f"{x},{y} : {n}")
            # Plus 1 because we are working on the buffered version
            if is_corner(x, y, len(frames[now][0]) - 2):
                frames[now][y + 1][x + 1] = 1
            elif c:
                frames[now][y+1][x+1] = 1 if n == 2 or n == 3 else 0
            else:
                frames[now][y+1][x+1] = 1 if n == 3 else 0
    #print(f"after {now} steps")
    #print(frames[now])

print(f"part 1 answer: {np.sum(frames[frame_size-1])}")

visualize_lights(frames)


