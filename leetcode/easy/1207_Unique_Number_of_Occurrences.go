// https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

package main

import "fmt"

func uniqueOccurrences(arr []int) bool {
	occurrencesMap := map[int]int{}
	numbersMap := map[int]struct{}{}

	for _, v := range arr {
		occurrencesMap[v]++
	}

	for _, v := range occurrencesMap {
		if _, ok := numbersMap[v]; ok {
			return false
		} else {
			numbersMap[v] = struct{}{}
		}
	}

	return true
}

func main() {
	fmt.Println(uniqueOccurrences([]int{1, 2}))
}
