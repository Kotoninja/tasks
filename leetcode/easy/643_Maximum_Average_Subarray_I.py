# https://leetcode.com/problems/maximum-average-subarray-i/description/


def findMaxAverage(nums: list[int], k: int) -> float:
    n = len(nums)
    sum = 0

    for i in range(k):
        sum += nums[i]

    max_sum = sum
    for i in range(k, n):
        sum += nums[i]
        sum -= nums[i - k]
        max_sum = max(max_sum, sum)
    return max_sum / k


print(findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
print(findMaxAverage(nums = [-1], k = 1))
