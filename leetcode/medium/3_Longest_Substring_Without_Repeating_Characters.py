# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    answer = 1

    r, l = 0, 1

    n = len(s)
    while l < n:
        if s[l] in s[r:l]:
            r += 1
        else:
            l += 1
            answer = max(answer, len(s[r:l]))
    return answer


print(lengthOfLongestSubstring(s="abcabcbb"))
print(lengthOfLongestSubstring(s="a"))
print(lengthOfLongestSubstring(s="aaaa"))
print(lengthOfLongestSubstring(s="bbbb"))
print(lengthOfLongestSubstring(s="abcb"))
print(lengthOfLongestSubstring(s="ababab"))
