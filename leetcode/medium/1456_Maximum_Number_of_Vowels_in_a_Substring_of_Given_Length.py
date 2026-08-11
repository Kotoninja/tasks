# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75


def maxVowels(s: str, k: int) -> int:
    max_vowel_seq = 0

    l, r = 0, 0
    inter_vowel = 0
    while l <= r < len(s):
        letter = s[r]

        if letter in "aeiuo":
            inter_vowel += 1

        if r - l == k - 1:
            max_vowel_seq = max(max_vowel_seq, inter_vowel)
            if s[l] in "aeiuo":
                inter_vowel -= 1
            l += 1
            r += 1
        else:
            r += 1

    return max_vowel_seq


print(maxVowels(s="abciiidef", k=3))
print(maxVowels(s="aeiou", k=2))
print(maxVowels(s="leetcode", k=3))
