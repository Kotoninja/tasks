# https://leetcode.com/problems/reshape-the-matrix/description/?envType=problem-list-v2&envId=array

import itertools


def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    if len(mat) * len(mat[0]) != r * c:
        return mat

    arr = list(itertools.chain(*mat))

    result = []

    for _ in range(r):
        slice = c
        result.append(arr[:slice])
        arr = arr[slice:]

    return result


print(matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4))
print(matrixReshape(mat=[[1, 2]], r=1, c=1))
print(
    matrixReshape(
        mat=[
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
        ],
        r=42,
        c=5,
    )
)
print(matrixReshape([[1,2],[3,4]], r=4, c=1))
print(matrixReshape([[1,2]], r=1, c=1))

