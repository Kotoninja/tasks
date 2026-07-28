# https://leetcode.com/problems/container-with-most-water/
def maxArea(height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    max_water = 0

    while left < right:
        max_water = max(max_water, (right - left) * min(height[right], height[left]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
