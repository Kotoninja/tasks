# https://leetcode.com/problems/longest-consecutive-sequence/description/
"""
nums = [100, 4, 200, 1, 3, 2]

i = 0
number = 100
map = {100: 1}

i = 1
number = 4
map = {100: 1, 4: 1}

i = 2
number = 200
map = {100: 1, 4: 1, 200: 1}

i = 3
number = 1
map = {100: 1, 4: 1, 200: 1, 1: 1}

i = 4
number = 3
map = {100: 1, 4: 2, 200: 1, 1: 1, 3: 1}

i = 5
number = 2
map = {100: 1, 4: 4, 200: 1, 1: 1, 3: 3, 2: 2}
"""


def longestConsecutive(nums: list[int]) -> int:
    # TLE
    # if not nums:
    #     return 0

    # hash_map: dict = {}

    # def ancestors_update(number: int) -> int:
    #     nonlocal hash_map
    #     if number - 1 in hash_map:
    #         return ancestors_update(number - 1)
    #     return number - 1

    # def descendants_update(number: int) -> int:
    #     nonlocal hash_map
    #     if (number + 1) in hash_map:
    #         hash_map[number + 1] = hash_map[number] + 1
    #         return descendants_update(number + 1)
    #     return number + 1

    # for number in nums:
    #     if not hash_map:
    #         hash_map[number] = 1
    #         continue

    #     if ancestors_update(number) == number - 1:
    #         hash_map[number] = 1
    #     else:
    #         hash_map[number] = 1 + hash_map[number - 1]

    #     descendants_update(number)

    # return max(hash_map.values())

    nums_set = set(nums)

    def descendant_length(number):
        if number + 1 in nums_set:
            return 1 + descendant_length(number + 1)
        return 1

    max_length = 0

    for number in nums_set:
        if number - 1 not in nums_set:
            inter_length = descendant_length(number)
            max_length = max(inter_length, max_length)

    return max_length


print(longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
