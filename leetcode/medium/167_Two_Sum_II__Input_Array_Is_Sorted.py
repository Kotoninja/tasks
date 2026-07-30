# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


def twoSum(numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l + 1, r + 1]


print(twoSum(numbers=[2, 7, 11, 15], target=9))
print(twoSum(numbers=[2, 3, 4], target=6))
print(twoSum(numbers=[-1, 0], target=-1))
