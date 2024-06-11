#!/usr/bin/python3

''' This mudle contains the function island_perimeter '''


def island_perimeter(grid):
    ''' Calculates the perimeter of an island
                    (a series of 1s inside a 2d matrix surrounded by 0s) '''
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue

            # If there is a 0(or nothing) above the one, add 1 to the perimeter
            if i == 0 or grid[i - 1][j] == 0:
                perimeter += 1

            # If there is 0(or nothing) to the left of the one, add 1 to the
            # perimeter
            if j == 0 or grid[i][j - 1] == 0:
                perimeter += 1

            # If there is 0(or nothing) to the right of the one, add 1 to the
            # perimeter
            if (j == len(grid[i]) - 1) or grid[i][j + 1] == 0:
                perimeter += 1

            # If there is 0(or nothing) to the bottom of the one, add 1 to the
            # perimeter
            if (i == len(grid) - 1) or grid[i + 1][j] == 0:
                perimeter += 1

    return perimeter
