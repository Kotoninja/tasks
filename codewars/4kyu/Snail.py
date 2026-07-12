"""
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

"""


def snail(snail_map: list[list]):
    answer: list[int] = []

    step: int = 0
    length = len(snail_map)

    if snail_map[0]:
        for i in range(length):
            print("way", i + 1)

            top = i
            bottom = length - step - 1

            if (top == bottom):
                answer.append(snail_map[top][bottom])
            else:
                answer += snail_map[top][0 + i : len(snail_map[top]) - i]

                for right_index in range(1 + i, length - 1 - i):
                    slice = snail_map[right_index]
                    answer.append(slice[length - 1 - i])

                answer += snail_map[bottom][0 + i : len(snail_map[bottom]) - i][::-1]

                for left_index in range(1 + i, length - 1 - i):
                    slice = snail_map[::-1][left_index]
                    answer.append(slice[i])

            # next iteration
            if i < length // 2:
                step += 1
            else:
                break
    return answer


# print(
#     snail(
#         [
#             [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#             [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
#             [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#             [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#             [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
#             [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
#             [7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
#             [8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
#             [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
#         ]
#     )
# )
# print(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# print(snail([[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 7], [7, 8, 9, 7]]))
print(snail([[1]]))
# print(
#     snail(
#         [
#             [5, 3, 8, 6, 4, 4, 2, 6, 9, 1],
#             [6, 5, 9, 5, 6, 7, 2, 7, 9, 4],
#             [9, 3, 5, 5, 8, 4, 7, 6, 7, 6],
#             [5, 4, 1, 4, 3, 2, 2, 2, 2, 9],
#             [2, 8, 3, 3, 4, 3, 6, 1, 7, 4],
#             [9, 3, 1, 3, 8, 8, 3, 9, 7, 1],
#             [1, 2, 8, 6, 5, 3, 2, 5, 2, 6],
#             [8, 8, 4, 9, 2, 8, 5, 2, 6, 7],
#             [3, 8, 2, 7, 8, 9, 5, 2, 9, 4],
#             [6, 4, 7, 3, 4, 2, 6, 4, 3, 1],
#         ]
#     )
# )

# Tests
# def new_func(snail):
#     array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#     expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
#     assert snail(array) == expected

#     array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
#     expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     assert snail(array) == expected


# assert new_func(snail)
