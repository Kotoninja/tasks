# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=programming-skills


def mergeAlternately(word1: str, word2: str) -> str:
    answer = ""
    for i,j in zip(word1,word2):
        answer += i
        answer += j
        
    if len(word1) - len(word2) > 0:
        answer += word1[len(word2):]
        
    elif len(word1) - len(word2) < 0:
        answer += word2[len(word1):]

    return answer
    
    
print(mergeAlternately(word1 = "abc", word2 = "pqrs"))
print(mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(mergeAlternately(word1 = "abcd", word2 = "pq"))