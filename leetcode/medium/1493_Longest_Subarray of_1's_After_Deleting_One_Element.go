// https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

package main

import "fmt"

func longestSubarray(nums []int) int {
	var zeroCount int
	var answer int

	for l, r := 0, 0; r < len(nums); r++ {
		if nums[r] == 0 {
			zeroCount++
		}
		if zeroCount < 2 {
			answer = max(answer, r-l)
		}

		for zeroCount > 1 {
			if nums[l] == 0 {
				zeroCount--
			}
			l++
		}
	}

	return answer

}

func main() {
	fmt.Println(longestSubarray([]int{1, 1, 0, 1}))
	fmt.Println(longestSubarray([]int{0, 1, 1, 1, 0, 1, 1, 0, 1}))
	fmt.Println(longestSubarray([]int{1, 0, 0, 0, 0}))
	// fmt.Println(longestSubarray([]int{1, 1, 0, 1}))
}
