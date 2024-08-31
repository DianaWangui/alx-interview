#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
        that returns the perimeter of the island described in grid:

        grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
    """
    count = 0
    for column in range(len(grid)):
        for row in range(len(grid[column])):
            if grid[column][row] == 1:
                if column - 1 < 0:
                    count += 1
                else:
                    try:
                        if grid[column - 1][row] == 0 or column - 1 < 0:
                            count += 1
                    except Exception:
                        pass
                if column + 1 > len(grid) - 1:
                    count += 1
                else:
                    try:
                        if grid[column + 1][row] == 0:
                            count += 1
                    except Exception:
                        pass
                """heck right"""
                if row + 1 > len(grid[column]) - 1:
                    count += 1
                else:
                    try:
                        if grid[column][row + 1] == 0:
                            count += 1
                    except Exception:
                        pass
                # check left
                try:
                    if grid[column][row - 1] == 0 or row - 1 < 0:
                        count += 1
                except Exception:
                    pass
    return count
