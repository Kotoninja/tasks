# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75


def longestOnes(nums: list[int], k: int) -> int:
    l, r = 0, 0

    longest_seq = 0

    while l <= r:
        if r == len(nums):
            longest_seq = max(longest_seq, r - l)
            break
        if not nums[r]:
            k -= 1

        if k <= 0:
            longest_seq = max(longest_seq, r - l)
            while k < 0:
                if not nums[l]:
                    k += 1
                l += 1
        r += 1
    if not l and r == len(nums):
        return len(nums)
    return longest_seq


print(longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
print(longestOnes(nums=[0, 0, 0, 1], k=4))
print(longestOnes(nums=[0, 0, 1, 1], k=1))
