# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75


def maxOperations(nums: list[int], k: int) -> int:
    hash_map = {}

    answer = 0
    for number in nums:
        if k - number in hash_map:
            hash_map[k - number] -= 1

            answer += 1

            if hash_map[k - number] == 0:
                del hash_map[k - number]

        else:
            hash_map[number] = hash_map.get(number, 0) + 1

    return answer

    # Two Pointers Solution
    # nums.sort()

    # l = 0
    # r = len(nums) - 1

    # count = 0
    # while l < r:
    #     calculate = nums[l] + nums[r]
    #     if calculate == k:
    #         count += 1
    #         l += 1
    #         r -= 1
    #     elif calculate > k:
    #         r -= 1
    #     else:
    #         l += 1
    # return count


print(maxOperations(nums=[1, 2, 3, 4], k=5))
print(maxOperations(nums=[3, 1, 3, 4, 3], k=6))
print(
    maxOperations(
        nums=[2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], k=3
    )
)
