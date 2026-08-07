# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=programming-skills

def lengthOfLastWord(s: str) -> int:
    return len(s.rstrip().split()[-1])


print(lengthOfLastWord(s = "Hello World"))
print(lengthOfLastWord(s = "   fly me   to   the moon  "))