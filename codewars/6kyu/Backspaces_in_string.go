package main

import (
	"fmt"
	"strings"
)

func CleanString(s string) string {

	symbols := []string{}

	for _, letter := range s {
		switch string(letter) {
		case "#":
			if len(symbols) > 0 {
				symbols = symbols[:len(symbols)-1]
			}
		default:
			symbols = append(symbols, string(letter))
		}
	}

	return strings.Join(symbols, "")
}

func main() {
	fmt.Println(CleanString("abc#d##c"))
	fmt.Println(CleanString("abc##d######"))
	fmt.Println(CleanString("#######"))
	fmt.Println(CleanString(""))
}
