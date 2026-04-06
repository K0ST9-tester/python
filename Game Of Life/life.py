import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

HEIGHT, WIDTH = 50, 50

grid = np.random.randint(0, 2, (HEIGHT, WIDTH))


def count_neighbors(grid, x, y):    
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1),  (0, 1),  (1, 1)
    ]

    count = 0

    for dx, dy in directions:
        nx = (x + dx) % WIDTH
        ny = (y + dy) % HEIGHT
        count += grid[ny][nx]

    return count

def update(grid):
    new_grid = np.zeros_like(grid)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(grid, x, y)

            if grid[y][x] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[y][x] = 0
                else:
                    new_grid[y][x] = 1
            else:
                if neighbors == 3:
                    new_grid[y][x] = 1
    
    return new_grid


def animate(frame):
    global grid
    grid = update(grid)
    img.set_data(grid)
    return [img]


fig, ax = plt.subplots()
img = ax.imshow(grid)
ani = FuncAnimation(fig, animate, interval = 50)
ax.axis('off')

plt.show()