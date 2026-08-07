# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=programming-skills


def romanToInt(s: str) -> int:
    hash_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and hash_map[s[i]] < hash_map[s[i + 1]]:
            res -= hash_map[s[i]]
        else:
            res += hash_map[s[i]]
    return res
