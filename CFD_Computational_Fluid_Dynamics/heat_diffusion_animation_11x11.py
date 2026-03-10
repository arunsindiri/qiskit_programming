import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# ----------------------------
# Create 11x11 grid
# ----------------------------
grid = np.zeros((11,11))
grid[5,5] = 100

iteration = 0

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

# ----------------------------
# Draw grid function
# ----------------------------
def draw_grid():

    ax.clear()

    ax.imshow(grid, cmap="inferno", vmin=0, vmax=100)

    # show values
    for i in range(11):
        for j in range(11):

            value = grid[i,j]
            color = "white" if value < 50 else "black"

            ax.text(
                j,
                i,
                f"{value:.1f}",
                ha="center",
                va="center",
                color=color,
                fontsize=8
            )

    ax.set_title(f"Heat Diffusion Iteration {iteration}")

    fig.canvas.draw()


# ----------------------------
# Next iteration logic
# ----------------------------
def next_iteration(event):

    global grid
    global iteration

    new_grid = grid.copy()

    for i in range(11):
        for j in range(11):

            total = 0
            count = 0

            if i > 0:
                total += grid[i-1, j]
                count += 1

            if i < 10:
                total += grid[i+1, j]
                count += 1

            if j > 0:
                total += grid[i, j-1]
                count += 1

            if j < 10:
                total += grid[i, j+1]
                count += 1

            new_grid[i,j] = total / count

    grid[:] = new_grid
    iteration += 1

    draw_grid()


# ----------------------------
# Button UI
# ----------------------------
ax_button = plt.axes([0.45, 0.05, 0.1, 0.075])
next_button = Button(ax_button, "Next")

next_button.on_clicked(next_iteration)

# initial draw
draw_grid()

plt.show()
