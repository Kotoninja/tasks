# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=programming-skills


def setZeroes(matrix: list[list[int]]) -> list[list[int]]:
    row = set()
    column = set()
    m = len(matrix[0])
    n = len(matrix)

    for i in range(n):
        for j in range(m):
            if not matrix[i][j]:
                row.add(i)
                column.add(j)

    for change in row:
        matrix[change] = [0] * m

    for change in column:
        for i in range(n):
            matrix[i][change] = 0

    return matrix


# print(setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
# print(setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
# print(setZeroes(matrix=[[1]]))
# print(setZeroes(matrix=[[0]]))
print(
    setZeroes(
        matrix=[
            [1, 2, 3, 4],
            [5, 0, 7, 8],
            [0, 10, 11, 12],
            [13, 14, 15, 0],
        ]
    )
)
