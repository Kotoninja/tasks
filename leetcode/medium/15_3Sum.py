# https://leetcode.com/problems/3sum/description/


def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()

    answer = []

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            calculation = nums[i] + nums[left] + nums[right]

            if calculation == 0:
                answer.append([nums[i], nums[left], nums[right]])

                left, right = left + 1, right - 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif calculation < 0:
                left += 1
            else:
                right -= 1
    return answer


# print(threeSum(nums=[-4, -1, -1, 0, 1, 2]))
# print(threeSum(nums=[0, 1, 2, 3, 4]))
# print(threeSum(nums=[0, 0, 0]))
# print(threeSum(nums=[0, 1, 1]))
# print(threeSum(nums=[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
# print(threeSum(nums=[-1, 0, 1]))
# print(threeSum(nums=[0, 0, 0, 0]))
print(threeSum(nums=[-100, -70, -60, 110, 120, 130, 160]))


