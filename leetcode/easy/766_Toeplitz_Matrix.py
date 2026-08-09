# https://leetcode.com/problems/toeplitz-matrix/description/?envType=problem-list-v2&envId=array


def isToeplitzMatrix(matrix: list[list[int]]) -> bool:
    def diagonal_check(i, j):
        if i < 0 or i >= len(matrix) - 1 or j < 0 or j >= len(matrix[0]) - 1:
            return 0
        if matrix[i][j] == matrix[i + 1][j + 1]:
            return 0 + diagonal_check(i + 1, j + 1)

        else:
            return 1

    for j in range(len(matrix[0])):
        if diagonal_check(0, j):
            return False

    for i in range(1, len(matrix)):
        if diagonal_check(i, 0):
            return False
    return True


print(isToeplitzMatrix(matrix=[[1, 2], [2, 2]]))
print(isToeplitzMatrix(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(
    isToeplitzMatrix(
        [
            [36, 59, 71, 15, 26, 82, 87],
            [56, 36, 59, 71, 15, 26, 82],
            [15, 0, 36, 59, 71, 15, 26],
        ]
    )
)
