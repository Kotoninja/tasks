# https://leetcode.com/problems/two-sum/description/


def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}

    for index, value in enumerate(nums):
        hash_map[value] = index

    for i in range(len(nums)):
        number = nums[i]
        if hash_map.get(target - number):
            hash_index = hash_map[target - number]
            if i != hash_index:
                return [i, hash_map[target - number]]
    return []


assert twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert twoSum(nums=[3, 3], target=6) == [0, 1]
assert twoSum(nums=[3, 2, 2, 3], target=6) == [0, 3]
