# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75


def reverseVowels(s: str) -> str:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

    list_s = list(s)
    l = 0
    r = len(s) - 1

    while l < r:
        left_letter = list_s[l]
        right_letter = list_s[r]

        if left_letter not in vowels:
            l += 1
        if right_letter not in vowels:
            r -= 1

        if left_letter in vowels and right_letter in vowels:
            list_s[l], list_s[r] = list_s[r], list_s[l]
            l += 1
            r -= 1
    return "".join(list_s)


print(reverseVowels(s="IceCreAm"))
print(reverseVowels(s="leetcode"))
