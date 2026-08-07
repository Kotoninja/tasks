# https://leetcode.com/problems/find-the-difference/description/?envType=study-plan-v2&envId=programming-skills

def findTheDifference(s: str, t: str) -> str:
    hash_map = {}
    
    for letter in s:
        hash_map[letter] = hash_map.get(letter, 0) + 1
        
    for letter in t:
        if letter in hash_map:
            hash_map[letter] -=1
            if not hash_map[letter]:
                hash_map.pop(letter)
        else:
            return letter
print(findTheDifference(s = "abcd", t = "abcde"))
print(findTheDifference(s = "aaa", t = "aa"))