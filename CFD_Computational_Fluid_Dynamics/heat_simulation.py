import numpy as np

grid = np.zeros((5,5))

grid[2,2] = 100

for step in range(10):

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
    print(grid, "\n")

print(grid)
