def fourSum(nums: list[int], target: int) -> list[list[int]]:
    answer = []
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(n - 1, 0, -1):
            if j < n - 1 and nums[j] == nums[j + 1]:
                continue

            l = i + 1
            r = j - 1

            while l < r:
                calculation = nums[i] + nums[l] + nums[r] + nums[j]
                if calculation == target:
                    answer.append([nums[i], nums[l], nums[r], nums[j]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                elif calculation < target:
                    l += 1
                else:
                    r -= 1



    return answer


print(fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
print(fourSum(nums=[2, 2, 2, 2, 2], target=8))
print(fourSum(nums=[0,0,0,0], target=0))
print(fourSum(nums=[0,0,0], target=0))
print(fourSum(nums=[-2,-1,-1,1,1,2,2], target=0))
print(fourSum(nums=[2,4,0,4,-3,-3], target=0))
