package main

import (
	"fmt"
	"math"
)

func LeastLarger(a []int, i int) int {
	var result float64 = math.Inf(1)
	var result_index int = -1

	for ind, v := range a {
		if v != a[i] && v > a[i] {
			difference := math.Min(float64(result), float64(v))
			if difference != result {
				result = difference
				result_index = ind
			}
		}
	}
	return result_index
}

func main() {
	fmt.Println(LeastLarger([]int{1, 3, 5, 2, 4}, 0))
	fmt.Println(LeastLarger([]int{4, 1, 3, 5, 6}, 0))
}
