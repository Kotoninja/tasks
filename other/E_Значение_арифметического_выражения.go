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

var Priority = map[string]string{
	"+": "-*",
	"-": "+*",
	"*": "*",
}

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

func InfixToPostfix(infixCommand []string) []string {
	// 6 + 3 * ( 1 + 4 * 5 ) * 2
	n := len(infixCommand)
	answer := []string{}
	stack := []string{}

	for i := 0; i < n; i++ {
		symbol := infixCommand[i]
		switch symbol {
		case "+", "-":
			for len(stack) > 0 && strings.Contains(Priority[symbol], stack[len(stack)-1]) {
				answer = append(answer, stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, symbol)
		case "*":
			for len(stack) > 0 && strings.Contains(Priority[symbol], stack[len(stack)-1]) {
				answer = append(answer, stack[len(stack)-1])
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

func CalculateEpression(command []string) (int, error) {
	n := len(command)

	stack := []int{}

	for i := 0; i < n; i++ {
		symbol := command[i]

		isOperation := strings.Contains("+-*", symbol)

		if !isOperation {
			digit, err := strconv.Atoi(symbol)
			if err != nil {
				return 0, err
			}
			stack = append(stack, digit)
			continue
		}

		if isOperation && len(stack) < 2 {
			return 0, errors.New("STACK LT 2")
		}

		first := stack[len(stack)-1]
		second := stack[len(stack)-2]

		switch symbol {
		case "+":
			stack = append(stack[:len(stack)-2], second+first)
		case "-":
			stack = append(stack[:len(stack)-2], second-first)
		case "*":
			stack = append(stack[:len(stack)-2], second*first)

		default:
			return 0, errors.New("Error operation")
		}
	}

	if len(stack) != 1 {
		return 0, errors.New("len stack not equal 1")
	}
	return stack[0], nil
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	line := scanner.Text()

	listLine := ConvertStringToList(line)
	calculation, err := CalculateEpression(InfixToPostfix(listLine))
	if err != nil {
		fmt.Println("WRONG")
		return
	}

	fmt.Println(strconv.Itoa(calculation))
}
