# https://leetcode.com/problems/top-k-frequent-elements/description/


def topKFrequent(nums: list[int], k: int) -> list[int]:
    hash_map: dict = {}

    for i in nums:
        hash_map[i] = hash_map.get(i, 0) + 1

    array = [None] * (len(nums) + 1)
    for number, index in hash_map.items():
        if array[index] is not None:
            if isinstance(array[index], int):
                array[index] = [array[index], number]
            else:
                array[index].append(number)
        else:
            array[index] = number

    answer = []
    i = len(array) - 1
    while i != 0 and k != 0:
        if array[i] is not None:
            if isinstance(array[i], list):
                for num in array[i]:
                    answer.append(num)
                    if k == 0:
                        break
                    k -= 1
            else:
                answer.append(array[i])
                k -= 1

        # Next iteration
        i -= 1

    return answer


# second solution
# from collections import Counter


# def topKFrequent(nums: list[int], k: int) -> list[int]:
#     frequencies = Counter(nums)

#     return [part[0] for part in frequencies.most_common(k)]


# print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
# print(topKFrequent(nums=[1], k=1))
# print(topKFrequent(nums=[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k=2))
# print(topKFrequent(nums=[3,0,1,0], k=1))
print(
    topKFrequent(
        nums=[6, 0, 1, 4, 9, 7, -3, 1, -4, -8, 4, -7, -3, 3, 2, -3, 9, 5, -4, 0], k=6
    )
)
