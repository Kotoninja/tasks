// https://leetcode.com/problems/min-stack/description/

package main

type MinStack struct {
	mainStack []int
	minStack  []int
}

func Constructor() *MinStack {
	return &MinStack{mainStack: []int{}, minStack: []int{}}
}

func (this *MinStack) Push(value int) {
	this.mainStack = append(this.mainStack, value)
	if len(this.minStack) == 0 || this.minStack[len(this.minStack)-1] >= value {
		this.minStack = append(this.minStack, value)
	} else {
		this.minStack = append([]int{value}, this.minStack...)
	}
}

func (this *MinStack) Pop() {
	if len(this.mainStack) >= 1 {
		n := len(this.mainStack)
		popValue := this.mainStack[n-1]
		if popValue == this.minStack[n-1] {
			this.minStack = this.minStack[:n-1]
		} else {
			this.minStack = this.minStack[1:]
		}

		this.mainStack = this.mainStack[:n-1]
	}

}

func (this *MinStack) Top() int {
	return this.mainStack[len(this.mainStack)-1]

}

func (this *MinStack) GetMin() int {
	return this.minStack[len(this.minStack)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(value);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */

func main() {
	obj := Constructor()
	obj.Push(value)
	obj.Pop()
	param_3 := obj.Top()
	param_4 := obj.GetMin()
}
