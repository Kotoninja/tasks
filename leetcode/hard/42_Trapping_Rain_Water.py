# https://leetcode.com/problems/trapping-rain-water/description/


def trap(height: list[int]) -> int:
    answer = 0

    left, right = 0, len(height) - 1
    leftMax, rightMax = 0, 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > leftMax:
                leftMax = height[left]
            else:
                answer += leftMax - height[left]
            left += 1
        else:
            if height[right] > rightMax:
                rightMax = height[right]
            else:
                answer += rightMax - height[right]
            right -= 1
    return answer

print(trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 4]))
print(trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(trap(height=[4, 2, 0, 3, 2, 5]))
print(trap(height=[4, 2, 3]))
print(trap(height=[3, 2, 1, 2, 1]))
