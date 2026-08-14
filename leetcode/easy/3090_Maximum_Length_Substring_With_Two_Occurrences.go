package main

import (
	"fmt"
	"unicode/utf8"
)

func maximumLengthSubstring(s string) int {
	hashMap := map[byte]int{}

	var result int

	for r, l := 0, 0; r < utf8.RuneCountInString(s); r++ {
		hashMap[s[r]]++

		for hashMap[s[r]] > 2 && l < utf8.RuneCountInString(s) {
			hashMap[s[l]]--
			if hashMap[s[l]] == 0 {
				delete(hashMap, s[l])
			}
			l++
		}

		result = max(r-l+1, result)
	}

	return result
}

func main() {
	fmt.Println(maximumLengthSubstring("bcbbbcba"))
	fmt.Println(maximumLengthSubstring("aaaa"))
}
