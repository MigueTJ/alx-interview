#!/usr/bin/python3
'''calculate island perimter'''


def island_perimeter(grid):
    '''Return the perimeter of the island in the grid'''
    if not isinstance(grid, list):
        return 0

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
    return perimeter
