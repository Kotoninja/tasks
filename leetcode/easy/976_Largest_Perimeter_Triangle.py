# https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=study-plan-v2&envId=programming-skills


def largestPerimeter(nums: list[int]) -> int:
    nums = sorted(nums)[::-1]

    l = 0
    r = 2

    while r < len(nums):
        slice = nums[l : r + 1]

        for number in slice:
            if number >= sum(slice) - number:
                l += 1
                r += 1
                break
        else:
            return sum(slice)
    return 0


print(largestPerimeter(nums=[2, 1, 2]))
print(largestPerimeter(nums=[1, 2, 1, 10]))
