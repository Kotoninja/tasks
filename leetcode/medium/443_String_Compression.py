# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75


def compress(chars: list[str]) -> int:
    i = 0

    count = 1
    while i < len(chars) - 1:
        if chars[i + 1] == chars[i]:
            del chars[i + 1]
            count += 1
        elif count > 1:
            chars[i + 1 : i + 1] = list(str(count))
            i += len(str(count)) + 1
            count = 1
        else:
            count = 1
            i += 1
    if count > 1:
        chars[len(chars) :] = list(str(count))
    return len(chars)


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(
    compress(
        [
            "a",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "c",
        ]
    )
)
print(
    compress(
        [
            "a",
            "a",
            "a",
            "a",
            "a",
            "a",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "b",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
            "c",
        ]
    )
)
