package kata

func CountPositivesSumNegatives(numbers []int) []int {
	var res []int

	countPositive := 0
	sumNegotive := 0

	for _, number := range numbers {
		if number <= 0 {
			sumNegotive += number
		} else {
			countPositive++
		}
	}
	res = append(res, countPositive, sumNegotive)

	return res
}
