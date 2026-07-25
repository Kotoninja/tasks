# https://www.codewars.com/kata/5a793fdbfd8c06d07f0000d5/train/python


def solve(st: str) -> str:

    exp: list[str] = st.translate({ord("("): " ", ord(")"): " "}).rstrip()[::-1].split()

    result: str = ""

    for value in exp:
        if value[0].isdigit():
            result *= int(value[0])
            if len(value) > 1:
                result = value[1::][::-1] + result
        else:
            result = value[::-1] + result
    return result
