# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/?envType=problem-list-v2&envId=hash-table


def maxSubarrayLength(nums: list[int], k: int) -> int:
    if len(nums) == 1 and k == 1:
        return 1

    hash_map = {}

    answer = 0
    l, r = 0, 0

    while r < len(nums):
        number = nums[r]

        if number not in hash_map:
            hash_map[number] = k - 1
        else:
            hash_map[number] -= 1

        if hash_map[number] < 0:
            answer = max(answer, r - l)
            while nums[l] != number:
                hash_map[nums[l]] += 1
                l += 1
            l += 1
            hash_map[number] += 1

        r += 1
    else:
        answer = max(answer, r - l)
    return answer


# print(maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
# print(maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
# print(maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
print(maxSubarrayLength(nums=[3,1,1], k=1))
