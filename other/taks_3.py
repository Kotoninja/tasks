import math

# t = int(input())


def algo(number: int):
    number_length = (math.floor(math.log10(number)) + 1) // 2

    if not (number // 10):
        return number

    return algo(int(str(number)[:number_length]) + int(str(number)[number_length:]))


# for i in range(t):
#     n = int(input())
#     print(algo(n))

assert algo(60) == 6
assert algo(12345) == 6
assert algo(2) == 2
assert algo(234527) == 54
