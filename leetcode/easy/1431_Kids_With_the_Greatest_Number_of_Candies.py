# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75


def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    max_candie = max(candies)

    return [candie + extraCandies >= max_candie for candie in candies]


print(kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
print(kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
print(kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
