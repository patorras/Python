
grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]



for y in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][y], end="")
    print("\n")
