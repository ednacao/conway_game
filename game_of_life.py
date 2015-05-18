"""Conway's Game of Life

Rules:
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overcrowding.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

Logic:
For any cell in the middle of a 3x3 grid, number of live cells accompanying it has to be
>= 2 and <= 3.

If each cell is represented by 0 or 1, then the sum of surrounding cells is 8.

Use numpy to create a grid of N x N."""


import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

N = 100
ON = 255
OFF = 0
a = [ON, OFF]

grid = np.random.choice(a, N*N, p=[0.1, 0.9]).reshape(N, N)


def permutation(data):
    global grid
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Add sum of surrounding cells
            grid_sum = (grid[i, (j-1) % N] +
                   grid[i, (j+1) % N] +
                   grid[(i-1) % N, j] +
                   grid[(i+1) % N, j] +
                   grid[(i-1) % N, (j-1) % N] +
                   grid[(i-1) % N, (j+1) % N] +
                   grid[(i+1) % N, (j-1) % N] +
                   grid[(i+1) % N, (j+1) % N]) / 255

        # Implement rules
        if grid[i, j] == ON:
            if (grid_sum < 2) or (grid_sum > 3):
              new_grid[i, j] = OFF
        else:
            if grid_sum == 3:
                new_grid[i, j] = ON

    # Update grid with new permutation
    mat.set_data(new_grid)
    grid = new_grid
    return [mat]

# Animate
fig, ax = plot.subplots()
mat = ax.matshow(grid)
animate = animation.FuncAnimation(fig, permutation, interval=50,
                              save_count=50)

plot.show()
