class Tree:
    def __init__(self, value) -> None:
        self.root = value
        self.right = None
        self.left = None

    def add_child(self, number):
        if number < self.root:
            if self.left is None:
                self.left = Tree(number)
            else:
                self.left.add_child(number)
        if number > self.root:
            if self.right is None:
                self.right = Tree(number)
            else:
                self.right.add_child(number)

    def get_length(self):
        left = self.left.get_length() if self.left else 0
        right = self.right.get_length() if self.right else 0
        return 1 + max(left, right)


def main(nums: list):
    t = Tree(nums[0])
    for number in nums[1:]:
        if number:
            t.add_child(number)
        else:
            break
    return t.get_length()


if __name__ == "__main__":
    print(main(nums=list(map(int, input().split()))))
