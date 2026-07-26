n = int(input())
array = list(map(int, input().split()))


class OneOfTwoZero(Exception): ...


while True:
    f_number, s_number = map(int, input().split())

    if not f_number and not s_number:
        break

    if not f_number and s_number or not s_number and f_number:
        raise OneOfTwoZero(f"f - {f_number} : s - {s_number}")

    array = [
        *array[: f_number - 1],
        *array[f_number - 1 : s_number][::-1],
        *array[s_number:],
    ]

print(array)
