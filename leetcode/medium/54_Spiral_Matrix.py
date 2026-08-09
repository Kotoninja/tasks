# https://leetcode.com/problems/spiral-matrix/description/?envType=study-plan-v2&envId=programming-skills


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    answer = []

    m = len(matrix[0])
    n = len(matrix)

    for i in range(len(matrix) // 2 + (1 if n % 2 else 0)):
        if i >= m or m - i - 1 < m // 2:
            break

        answer.extend(matrix[i][i : m - i])
        answer.extend([matrix[j][m - 1 - i] for j in range(1 + i, n - 1 - i)])
        if i != n - 1 - i:
            answer.extend(matrix[n - 1 - i][i : m - i][::-1])
        if i != m - 1 - i:
            answer.extend([matrix[j][i] for j in range(1 + i, n - 1 - i)][::-1])
    return answer


print(spiralOrder([[7], [9], [6]]))
print(spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]))
print(
    spiralOrder(
        [
            [1, 11],
            [2, 12],
            [3, 13],
            [4, 14],
            [5, 15],
            [6, 16],
            [7, 17],
            [8, 18],
            [9, 19],
            [10, 20],
        ]
    )
)
# print(
#     spiralOrder(
#         [
#             [1, 2, 3, 4],
#             [5, 6, 7, 8],
#             [9, 10, 11, 12],
#             [13, 14, 15, 16],
#             [17, 18, 19, 20],
#             [21, 22, 23, 24],
#         ]
#     )
# )
# print(spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(spiralOrder(matrix=[[5]]))
# print(spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# print(
#     spiralOrder(
#         matrix=[
#             [1, 2, 3, 4, 1, 2, 3, 4],
#             [5, 6, 7, 8, 5, 6, 7, 8],
#             [9, 10, 11, 12, 9, 10, 11, 12],
#             [1, 2, 3, 4, 1, 2, 3, 4],
#             [5, 6, 7, 8, 5, 6, 7, 8],
#             [9, 10, 11, 12, 9, 10, 11, 12],
#         ]
#     )
# )
