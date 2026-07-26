n, q = map(int, input().split())


def xor(array: list) -> int:
    result = array[0]
    for number in array[1:]:
        result ^= number

    return result


array: list[int] = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())

    slice = array[l - 1 : r]
    print(xor(slice))


# n, q = map(int, input().split())
# a = list(map(int, input().split()))

# # Вычисляем префиксные XOR
# prefix = [0] * (n + 1)
# for i in range(n):
#     prefix[i + 1] = prefix[i] ^ a[i]


# print(prefix)
# # Отвечаем на запросы
# for _ in range(q):
#     l, r = map(int, input().split())
#     # XOR на подотрезке [l, r] (1-индексация)
#     result = prefix[r] ^ prefix[l - 1]
#     print(result)
