import sys


def main():
    hash_map = dict()

    for _ in range(int(input())):
        words = input().split()
        hash_map[words[0]] = words[1]
        hash_map[words[1]] = words[0]

    return hash_map[input()]


if __name__ == "__main__":
    print(main())
