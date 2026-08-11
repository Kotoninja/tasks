# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75


def increasingTriplet(nums: list[int]) -> bool:
    min_number = float("inf")
    max_number = float("inf")

    for number in nums:
        if number <= min_number:
            min_number = number
        elif number <= max_number:
            max_number = number
        else:
            return True

    return False


print(increasingTriplet(nums=[1, 3, 2, 3, 4]))
print(increasingTriplet(nums=[5, 4, 3, 2, 1]))
print(increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))
print(increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))
print(increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))
