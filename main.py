from Functions import *

grid = [
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"]
]

heights = [0, 0, 0, 0, 0, 0, 0]

print_grid(grid)
while True:
    # player 1's turn
    print("player 1's turn")

    input_column = input("Enter column to place chip: ")
    while not input_chip(grid, heights, "1", input_column):
        print("Invalid move, please try again")
        input_column = input("Enter column to place chip: ")

    print("\n")
    print_grid(grid)

    if check_win(grid, input_column, heights[int(input_column) - 1]):
        print("player 1 wins")
        break

    # player 2's turn
    print("player 2's turn")

    input_column = input("Enter column to place chip: ")
    while not input_chip(grid, heights, "2", input_column):
        print("Invalid move, please try again")
        input_column = input("Enter column to place chip: ")

    print("\n")
    print_grid(grid)

    if check_win(grid, input_column, heights[int(input_column) - 1]):
        print("player 2 wins")
        break

    # if grid is filled
    if heights == [6, 6, 6, 6, 6, 6, 6]:
        print("It's a tie")
        break