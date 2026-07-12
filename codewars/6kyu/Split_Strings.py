# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python


def solution(s: str):
    answer: list[str] = []

    for i in range(0, len(s), 2):
        slice = s[i : i + 2]
        if len(slice) == 2:
            answer.append(slice)
        else:
            answer.append(slice + "_")

    return answer


# print(solution("abcdef"))
# print(solution("abc"))

assert solution("abc") == ["ab", "c_"]
assert solution("abcdef") == ["ab", "cd", "ef"]
