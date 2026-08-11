# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75


def gcdOfStrings(str1: str, str2: str) -> str:
    max_str, min_str = sorted([str1, str2])
    for i in range(len(min_str)):
        for j in range(len(min_str), i, -1):
            slice = min_str[i:j]
            if (
                not (len(min_str) % len(slice))
                and (slice * (len(min_str) // len(slice))) == min_str
                and not (len(max_str) % len(slice))
                and (slice * (len(max_str) // len(slice))) == max_str
            ):
                return slice
    return ""


print(gcdOfStrings(str1="ABCABC", str2="ABC"))
print(gcdOfStrings(str1="AA", str2="A"))
