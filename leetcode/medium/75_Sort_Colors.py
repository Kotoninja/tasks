# https://leetcode.com/problems/sort-colors/


def sortColors(nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            l, r = i, n - 1

            while l <= r:
                if nums[l] > nums[r]:
                    nums[l], nums[r] = nums[r], nums[l]
                r -= 1
        return nums


print(sortColors(nums=[2, 0, 2, 1, 1, 0]))
print(sortColors(nums=[2, 0, 1]))
