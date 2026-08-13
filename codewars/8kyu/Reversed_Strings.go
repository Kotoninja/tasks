package main

import "fmt"

func Solution(word string) string {
  var result string
  
  for i := len(word) - 1; i >= 0; i-- {
    result = result + string(word[i])
  }
  return result
}


func main() {
	fmt.Println(Solution("Hello"))
}