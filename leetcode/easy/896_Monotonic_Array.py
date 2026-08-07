# https://leetcode.com/problems/monotonic-array/description/?envType=study-plan-v2&envId=programming-skills

def isMonotonic(nums: list[int]) -> bool:
    if len(nums) == 1: return True

    if nums[-1] - nums[0] >= 0:
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return False
    else:
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                return False
    return True
print(isMonotonic([1,2,2,3]))