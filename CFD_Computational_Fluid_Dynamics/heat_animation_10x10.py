import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# create 11x11 grid
grid = np.zeros((11,11))

# heat source at the center
grid[5,5] = 100

fig, ax = plt.subplots()

def update(frame):
    global grid

    new_grid = grid.copy()

    for i in range(11):
        for j in range(11):

            total = 0
            count = 0

            # up
            if i > 0:
                total += grid[i-1, j]
                count += 1

            # down
            if i < 10:
                total += grid[i+1, j]
                count += 1

            # left
            if j > 0:
                total += grid[i, j-1]
                count += 1

            # right
            if j < 10:
                total += grid[i, j+1]
                count += 1

            new_grid[i,j] = total / count

    grid[:] = new_grid

    ax.clear()
    ax.imshow(grid, cmap='hot')
    ax.set_title(f"Iteration {frame}")

ani = animation.FuncAnimation(fig, update, frames=40, interval=300)

plt.show()
