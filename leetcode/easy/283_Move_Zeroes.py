# https://leetcode.com/problems/move-zeroes/
def moveZeroes(nums: list[int]) -> list[int]:
    count = len(nums) - 1

    i = 0
    while count:
        if not nums[i]:
            del nums[i]
            nums += [0]
        else:
            i += 1
        count -=1

    return nums
# print(moveZeroes([0, 1, 0, 3, 12]))
print(moveZeroes([0, 0, 0, 0, 0, 0, 1]))
