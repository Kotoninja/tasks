// https://leetcode.com/problems/daily-temperatures/description/
package main

import "fmt"

type Object struct {
	index int
	value int
}

func dailyTemperatures(temperatures []int) []int {
	stack := []Object{}

	answer := make([]int, len(temperatures))

	for i, v := range temperatures {
		obj := Object{index: i, value: v}

		if len(stack) == 0 {
			stack = append(stack, obj)
			continue
		}

		for len(stack) > 0 && obj.value > stack[len(stack)-1].value {
			temp := stack[len(stack)-1]
			answer[temp.index] = obj.index - temp.index
			stack = stack[:len(stack)-1]
		}

		stack = append(stack, obj)

	}

	return answer

}

func main() {
	fmt.Println(dailyTemperatures([]int{73, 74, 75, 71, 69, 72, 76, 73}))
	fmt.Println(dailyTemperatures([]int{30, 40, 50, 60}))
	fmt.Println(dailyTemperatures([]int{30, 60, 90}))
}
