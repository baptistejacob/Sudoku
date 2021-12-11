def solve(grid):
    position = find_empty_cell(grid)
    if not position:
        return True
    else:
        x, y = position

    for i in range(1, 10):
        if is_valid_nb_for_cell(grid, x, y, i):
            grid[x][y] = i

            if solve(grid):
                return True

            grid[x][y] = 0

    return False


def find_empty_cell(grid):
    """Find and empty cell in the grid return None if not found"""
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return (x, y)
    return None


def is_valid_nb_for_cell(grid, x, y, nb):
    """Check if a number is valid for x/y position in the grid"""
    # Check row and column
    for i in range(9):
        if grid[x][i] == nb or grid[i][y] == nb:
            return False

    # Check block
    x_off = (x // 3) * 3
    y_off = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[x_off + i][y_off + j] == nb:
                return False

    return True
