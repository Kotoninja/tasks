# https://leetcode.com/problems/valid-anagram/description/


def isAnagram(s: str, t: str) -> bool:
    dictionary: dict = {}

    for letter in s:
        dictionary[letter] = dictionary.get(letter, 0) + 1

    for letter in t:
        if letter not in dictionary or dictionary[letter] - 1 < 0:
            return False

        dictionary[letter] -= 1
        if dictionary[letter] == 0:
            dictionary.pop(letter)

    return not bool(dictionary)


# print(isAnagram(s="ab", t="a"))

# assert isAnagram(s="anagram", t="nagaram") == True
# assert isAnagram(s="rat", t="car") == False
