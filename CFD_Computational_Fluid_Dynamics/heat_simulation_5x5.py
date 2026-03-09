import numpy as np

grid = np.zeros((5,5))

grid[2,2] = 100

for step in range(10):

    new_grid = grid.copy()

    for i in range(5):
        for j in range(5):

            total = 0
            count = 0

            # up
            if i > 0:
                total += grid[i-1,j]
                count += 1

            # down
            if i < 4:
                total += grid[i+1,j]
                count += 1

            # left
            if j > 0:
                total += grid[i,j-1]
                count += 1

            # right
            if j < 4:
                total += grid[i,j+1]
                count += 1

            new_grid[i,j] = total / count

    grid = new_grid

print(grid)
