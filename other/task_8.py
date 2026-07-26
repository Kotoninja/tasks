# n = int(input())
# array = list(map(int, input().split()))

n = 5
array = [-4, -3, -1, -2, -5]
# array = [2, 3, -8, 7, -1, 2, 3]

shifted_array = [array[-1], *array[:-1]]

result: int = -10_001
for i in range(len(shifted_array)):
    for j in range(i + 1, len(shifted_array)):
        slice: list = shifted_array[i:j]
        if slice:
            result = max(result, sum(slice))

print(result)

# res = shifted_array[0]

# max_ending = shifted_array[0]

# for i in range(1, len(shifted_array)):
#     number = shifted_array[i]
#     max_ending = max(max_ending + number, number)

#     res = max(res, max_ending)

# print(res)
