package main

/*
Японский кроссворд — это головоломка, целью которой является получить черно-белую клетчатую картинку размера n × m n×m.
Загаданный японский кроссворд содержит пустое поле n × m n×m, некоторые клетки которого нужно покрасить в черный цвет.
Слева от каждой строки поля написана последовательность чисел.
Эти числа соответствуют длинам отрезков черных клеток в этой строке, перечисленным слева направо.
Аналогично над каждым столбцом написана последовательность чисел, соответствующих длинам черных отрезков в этом столбце, перечисленным сверху вниз.

Загаданный японский кроссворд:
*/

import (
	"bufio"
	"fmt"
	"os"
	// "strconv"
	// "strings"
)

func main() {
	var n, m int

	fmt.Scan(&n, &m)
	scanner := bufio.NewScanner(os.Stdin)

	crossword := []string{}

	for scanner.Scan() {
		text := scanner.Text()

		if len(text) == 0 {
			break
		}
		crossword = append(crossword, text)
	}

	// n, m := 11, 8
	// crossword := []string{
	// 	"........",
	// 	".####...",
	// 	".######.",
	// 	".##..##.",
	// 	".##..##.",
	// 	".######.",
	// 	".####...",
	// 	".##.....",
	// 	".##.....",
	// 	".##.....",
	// 	"........",
	// }
	// n := len(crossword)
	for _, line := range crossword {
		buf := []int{}
		frequency := 0
		for _, symbol := range line {
			if symbol == '.' {
				if frequency == 0 {
					continue
				} else {
					buf = append(buf, frequency)
					frequency = 0
				}
			} else {
				frequency++
			}
		}
		if frequency != 0 {
			buf = append(buf, frequency)
		}

		fmt.Printf("%d ", len(buf))
		for i, value := range buf {
			if i != len(buf) {
				fmt.Printf("%d ", value)
			} else {
				fmt.Printf("%d", value)
			}
		}
		fmt.Printf("\n")
		// fmt.Println(len(buf), buf)
	}
	fmt.Println()

	for line := range m {
		buf := []int{}
		frequency := 0
		for column := range n {
			symbol := crossword[column][line]
			if symbol == '.' {
				if frequency == 0 {
					continue
				} else {
					buf = append(buf, frequency)
					frequency = 0
				}
			} else {
				frequency++
			}
		}
		if frequency != 0 {
			buf = append(buf, frequency)
		}

		fmt.Printf("%d ", len(buf))
		for i, value := range buf {
			if i != len(buf) {
				fmt.Printf("%d ", value)
			} else {
				fmt.Printf("%d", value)
			}
		}
		fmt.Printf("\n")
	}

}
