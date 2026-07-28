# https://leetcode.com/problems/majority-element/description/


def majorityElement(nums: list[int]) -> int:
    hash_map: dict = {}

    for number in nums:
        hash_map[number] = hash_map.get(number, 0) + 1

    for number, count in hash_map.items():
        if count > len(nums) // 2:
            return number
    return 0


print(majorityElement(nums=[6, 5, 5]))
