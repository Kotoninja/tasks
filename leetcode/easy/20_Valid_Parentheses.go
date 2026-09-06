// https://leetcode.com/problems/valid-parentheses/description/

package main

import (
	"fmt"
	"strings"
)

func isValid(s string) bool {
	stack := []string{}

	brackets := map[string]string{
		"}": "{",
		"]": "[",
		")": "(",
	}

	for _, symbol := range s {
		// if len(stack) >= 1 {

		// 	fmt.Println(stack[len(stack)-1], brackets[string(symbol)])
		// }
		if strings.Contains("{([", string(symbol)) {
			stack = append(stack, string(symbol))
		} else if (len(stack) >= 1) && (stack[len(stack)-1] == brackets[string(symbol)]) {
			stack = stack[:len(stack)-1]
		} else {
			return false
		}
	}

	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("()"))
}
