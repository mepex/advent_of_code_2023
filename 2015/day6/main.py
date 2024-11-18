import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

size = 1000
f = "input.txt"


def process_inst(grid, inst):
    parts = inst.split()
    action = parts[0] if parts[0] == 'toggle' else ' '.join(parts[:2])
    start_x, start_y = map(int, parts[-3].split(','))
    end_x, end_y = map(int, parts[-1].split(','))

    if action == 'turn on':
        grid[start_x:end_x + 1, start_y:end_y + 1] = 1
    elif action == 'turn off':
        grid[start_x:end_x + 1, start_y:end_y + 1] = 0
    elif action == 'toggle':
        grid[start_x:end_x + 1, start_y:end_y + 1] = 1 - grid[start_x:end_x + 1, start_y:end_y + 1]

def process_inst2(grid, inst):
    parts = inst.split()
    action = parts[0] if parts[0] == 'toggle' else ' '.join(parts[:2])
    start_x, start_y = map(int, parts[-3].split(','))
    end_x, end_y = map(int, parts[-1].split(','))

    if action == 'turn on':
        grid[start_x:end_x + 1, start_y:end_y + 1] += 1
    elif action == 'turn off':
        grid[start_x:end_x + 1, start_y:end_y + 1] -= 1
        grid[grid < 0] = 0
    elif action == 'toggle':
        grid[start_x:end_x + 1, start_y:end_y + 1] += 2



def visualize_lights(instructions, vmax = 1):
    grid = np.zeros((size, size), dtype = int)
    fig, ax = plt.subplots()
    im = ax.imshow(grid, interpolation='none', aspect='auto', vmin=0, vmax=vmax)

    def update(frame):
        process_inst2(grid, instructions[frame])
        #im.set_data(grid)
        im.set_array(grid)
        ax.set_title(f"Step {frame}")
        #print(f"{frame}\n{im.get_array()}\n")
        return [im]

    ani = FuncAnimation(fig, update, frames=range(len(instructions)), interval=20, repeat=False)
    plt.show()


with open(f, 'r') as fp:
    instructions = fp.readlines()

idx = 0
grid = np.zeros((size, size), dtype=int)
for i in instructions:
    process_inst2(grid, i)

max = grid.max()

print(f"total: {grid.sum()}")
visualize_lights(instructions, max)
