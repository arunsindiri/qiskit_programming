import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid = np.zeros((5,5))
grid[2,2] = 100

fig, ax = plt.subplots()

def update(frame):
    global grid

    new_grid = grid.copy()

    for i in range(1,4):
        for j in range(1,4):

            new_grid[i,j] = (
                grid[i+1,j] +
                grid[i-1,j] +
                grid[i,j+1] +
                grid[i,j-1]
            ) / 4

    grid = new_grid

    ax.clear()
    ax.imshow(grid)
    ax.set_title(f"Iteration {frame}")

ani = animation.FuncAnimation(fig, update, frames=20, interval=500)

plt.show()
