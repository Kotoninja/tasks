package main

import "fmt"

func Cakes(recipe, available map[string]int) int {
	var answer int

MAINLOOP:
	for {
		for ingredient, count := range recipe {
			if availableCount, ok := available[ingredient]; ok && availableCount-count > 0 {
				available[ingredient] = availableCount - count
			} else {
				break MAINLOOP
			}
		}
		answer++
	}
	return answer
}

func main() {
	fmt.Println(Cakes(map[string]int{"flour": 500, "sugar": 200, "eggs": 1}, map[string]int{"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
}
