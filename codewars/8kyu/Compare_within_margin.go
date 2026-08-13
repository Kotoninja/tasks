package kyu

import "math"

func CloseCompare(a, b, margin float64) int {
	if margin >= 0 && margin >= math.Abs(a-b) {
		return 0
	}

	if a > b {
		return 1
	}
	return -1

}
