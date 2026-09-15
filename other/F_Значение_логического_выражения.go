// https://new.contest.yandex.ru/contests/97105/problems?id=30404%2F2023_01_18%2FHgDt2DvsLq
package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ConvertStringToList(line string) []string {
	answer := []string{}
	n := len(line)

	buf := ""
	for i := 0; i < n; i++ {
		symbol := string(line[i])

		if symbol == " " {
			continue
		}

		if symbol >= "0" && symbol <= "9" {
			buf += symbol
		} else {
			if buf != "" {
				answer = append(answer, buf)
				buf = ""
			}
			answer = append(answer, symbol)
		}
	}

	if buf != "" {
		answer = append(answer, buf)
	}

	return answer
}

var Priority = map[string]int{
	"!": 4,
	"&": 3,
	"|": 2,
	"^": 1,
	"(": 0,
}

func InfixToPostfix(infixCommand []string) []string {
	// 6 + 3 * ( 1 + 4 * 5 ) * 2
	n := len(infixCommand)
	answer := []string{}
	stack := []string{}

	for i := 0; i < n; i++ {
		symbol := infixCommand[i]
		switch symbol {
		case "|", "^", "&", "!":
			for len(stack) > 0 {
				pop := stack[len(stack)-1]

				if symbol == "!" {
					if Priority[symbol] < Priority[stack[len(stack)-1]] {
						answer = append(answer, pop)
					} else {
						break
					}
				} else {
					if Priority[symbol] <= Priority[stack[len(stack)-1]] {
						answer = append(answer, pop)
					} else {
						break
					}
				}

				stack = stack[:len(stack)-1]
			}
			stack = append(stack, symbol)

		case ")":
			for len(stack) > 0 && stack[len(stack)-1] != "(" {
				answer = append(answer, stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
			stack = stack[:len(stack)-1]
		case "(":
			stack = append(stack, symbol)
		default:
			answer = append(answer, symbol)
		}
	}

	for len(stack) != 0 {
		answer = append(answer, stack[len(stack)-1])
		stack = stack[:len(stack)-1]
	}

	return answer
}

func CalculateExpression(command []string) (bool, error) {
	n := len(command)

	stack := []bool{}

	for i := 0; i < n; i++ {
		symbol := command[i]

		isOperation := strings.Contains("!&|^", symbol)

		if !isOperation {
			digit, err := strconv.Atoi(symbol)
			if err != nil {
				return false, err
			}
			var val bool
			val = (digit != 0)
			stack = append(stack, val)
			continue
		}

		if symbol == "!" && len(stack) >= 1 {
			stack = append(stack[:len(stack)-1], !stack[len(stack)-1])
			continue
		}

		if isOperation && len(stack) < 2 {
			return false, errors.New("STACK LT 2")
		}

		first := stack[len(stack)-1]
		second := stack[len(stack)-2]

		switch symbol {
		case "&":
			stack = append(stack[:len(stack)-2], second && first)
		case "|":
			stack = append(stack[:len(stack)-2], second || first)
		case "^":
			stack = append(stack[:len(stack)-2], ((!first && second) || (first && !second)))

		default:
			return true, errors.New("Error operation")
		}
	}

	if len(stack) != 1 {
		return false, errors.New("len stack not equal 1")
	}
	return stack[0], nil
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()

	// expression = "1|(0&0^1)"
	// expression = "1"
	// expression = "!0"
	// expression = "!!1"
	// expression = "1&0"
	// expression = "1|0"
	// expression = "1^1"
	// expression = "1&0|1"
	// expression = "1|0&0"

	calc, _ := CalculateExpression(InfixToPostfix(ConvertStringToList(line)))

	if calc {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}
