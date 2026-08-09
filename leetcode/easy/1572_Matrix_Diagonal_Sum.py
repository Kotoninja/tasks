# https://leetcode.com/problems/matrix-diagonal-sum/description/?envType=study-plan-v2&envId=programming-skills


def diagonalSum(mat: list[list[int]]) -> int:
    n = len(mat)

    if len(mat[0]) == 1:
        return mat[0][0]

    def calculate(i, j, dirdirection):
        if i < 0 or i >= n or j < 0 or j >= n:
            return 0
        if dirdirection == "right":
            return mat[i][j] + calculate(i + 1, j + 1, dirdirection="right")
        elif dirdirection == "left":
            return mat[i][j] + calculate(i + 1, j - 1, dirdirection="left")
        return 0

    return (
        calculate(0, 0, "right")
        + calculate(0, n - 1, "left")
        - (mat[n // 2][n // 2] if len(mat[0]) % 2 else 0)
    )


print(diagonalSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonalSum(mat=[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))
print(diagonalSum(mat=[[5]]))
