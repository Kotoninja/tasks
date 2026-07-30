# https://leetcode.com/problems/valid-sudoku/description/
def isValidSudoku(board: list[list[str]]) -> bool:
    # row and column check
    for i in range(len(board)):
        # row check
        row_map = {}
        for row_number in board[i]:
            if row_number != ".":
                if row_number in row_map:
                    return False
                row_map[row_number] = 1
        # column check
        column_map = {}
        for j in range(len(board[i])):
            column_number = board[j][i]
            if column_number != ".":
                if column_number in column_map:
                    return False
                column_map[column_number] = 1
    #3x3 sub-boxes check
    for i in range(3):
        for row_step in range(3):
            three_map = {}
            for column_step in range(i % 3 * 3, i % 3 * 3 + 3):
                for number in board[column_step][
                    row_step % 3 * 3 : row_step % 3 * 3 + 3
                ]:
                    if number != ".":
                        if number not in three_map:
                            three_map[number] = 1
                        else:
                            return False
    return True


print(
    isValidSudoku(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
