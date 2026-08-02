# https://www.codewars.com/kata/541c8630095125aba6000c00
import math


def digital_root(n):
    if not int(math.log10(n)):
        return n
    return digital_root(sum([int(number) for number in str(n)]))


print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))