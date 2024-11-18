import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def process_instruction(grid, instruction):
    parts = instruction.split()
    action = parts[0] if parts[0] == 'toggle' else ' '.join(parts[:2])
    start_x, start_y = map(int, parts[-3].split(','))
    end_x, end_y = map(int, parts[-1].split(','))

    if action == 'turn on':
        grid[start_x:end_x + 1, start_y:end_y + 1] = 1
    elif action == 'turn off':
        grid[start_x:end_x + 1, start_y:end_y + 1] = 0
    elif action == 'toggle':
        grid[start_x:end_x + 1, start_y:end_y + 1] = 1 - grid[start_x:end_x + 1, start_y:end_y + 1]

def visualize_lights(instructions):
    grid = np.zeros((1000, 1000))

    fig, ax = plt.subplots()
    im = ax.imshow(grid, cmap='gray')

    def update(frame):
        process_instruction(grid, instructions[frame])
        im.set_data(grid)
        return [im]

    ani = FuncAnimation(fig, update, frames=range(len(instructions)), interval=200, blit=True)
    plt.show()

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        instructions = f.readlines()

    visualize_lights(instructions)