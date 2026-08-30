// https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
package main

import "fmt"

func Difference(a map[int]int, b map[int]int) []int {
	result := []int{}

	for element := range a {
		v, ok := b[element]
		fmt.Println(v, ok)
		if _, ok := b[element]; !ok {
			result = append(result, element)
		}
	}

	return result
}

func findDifference(nums1 []int, nums2 []int) [][]int {
	hashMapF := map[int]int{}
	hashMapS := map[int]int{}

	for _, f := range nums1 {
		hashMapF[f]++
	}

	for _, s := range nums2 {
		hashMapS[s]++
	}

	return [][]int{Difference(hashMapF, hashMapS), Difference(hashMapS, hashMapF)}
}

func main() {
	fmt.Println(findDifference([]int{1, 2, 3}, []int{2, 4, 6}))
}
