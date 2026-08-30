// https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

package main

import (
	"slices"
)

func equalPairs(grid [][]int) int {
	ans := 0

	n := len(grid)

	for r := range n {
		for c := range n {
			row := grid[r]

			column := []int{}

			for i := range n {
				column = append(column, grid[i][c])
			}
			if slices.Equal(row, column) {
				ans++
			}
		}
	}
	return ans
}
