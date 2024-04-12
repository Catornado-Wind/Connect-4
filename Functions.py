def print_grid(grid):
    """
    Prints the current grid state
    :param: grid: 2d array
    :return: None
    """

    for row in grid:
        for column in row:
            if column == "1":
                print(f"|\033[1;31mO\033[1;0m", end="")  # prints red O
            elif column == "2":
                print(f"|\033[1;34mO\033[1;0m", end="")  # prints blue 0
            else:
                print(f"|-", end="")

        print("|")

    print("-" * (2 * len(grid[0]) + 1))

    for column in range(1, len(grid[0]) + 1):
        print(f"|{column}", end="")

    print("|\n")


def input_chip(grid, heights, player, column):
    """
    Place the chips in the inputted column
    :param grid: 2d array
    :param heights: list (of integers)
    :param player: string ("1" or "2")
    :param column: string
    :return: bool
    """

    if column not in [str(i) for i in range(1, len(grid[0]) + 1)]:
        return False
    else:
        index_column = int(column) - 1

        if player == "1":
            # player 1
            if heights[index_column] >= len(grid):
                return False
            else:
                grid[5 - heights[index_column]][index_column] = "1"
                heights[index_column] += 1
                return True

        elif player == "2":
            # player 2
            if heights[index_column] >= len(grid):
                return False
            else:
                grid[5 - heights[index_column]][index_column] = "2"
                heights[index_column] += 1
                return True

        else:
            return False


def check_win(grid, column, height):
    """
    Check if a certain position have a winning line
    :param grid: 2d array
    :param column: string ("1" to "7")
    :param height: int (1 to 6)
    :return: bool
    """

    int_column = int(column)

    left_columns = int_column - 1 if int_column - 1 <= 3 else 3
    right_columns = len(grid[0]) - int_column if len(grid[0]) - int_column <= 3 else 3
    up_rows = len(grid) - height if len(grid) - height <= 3 else 3
    down_rows = height - 1 if height - 1 <= 3 else 3

    # check row
    for index_column in range(int_column - left_columns - 1, int_column + right_columns - 3):

        if grid[6 - height][index_column] == grid[6 - height][index_column + 1] == \
                grid[6 - height][index_column + 2] == grid[6 - height][index_column + 3]:
            return True

    # check column
    for index_row in range(6 - (height - down_rows), 8 - (height + up_rows), -1):

        if grid[index_row][int_column - 1] == grid[index_row - 1][int_column - 1] == \
                grid[index_row - 2][int_column - 1] == grid[index_row - 3][int_column - 1]:
            return True

    # check diagonal up
    min_row_column = min(left_columns, down_rows)
    max_row_column = min(right_columns, up_rows)

    for index in range(- min_row_column, max_row_column - 2):
        if grid[6 - height - index][int_column + index - 1] == grid[5 - height - index][int_column + index] == \
                grid[4 - height - index][int_column + index + 1] == grid[3 - height - index][int_column + index + 2]:
            return True

    # check diagonal down
    min_row_column = min(right_columns, down_rows)
    max_row_column = min(left_columns, up_rows)

    for index in range(- min_row_column, max_row_column - 2):
        if grid[6 - height - index][int_column - index - 1] == grid[5 - height - index][int_column - index - 2] == \
                grid[4 - height - index][int_column - index - 3] == grid[3 - height - index][int_column - index - 4]:
            return True

    return False