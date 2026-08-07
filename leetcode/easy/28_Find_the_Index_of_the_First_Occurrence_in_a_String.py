# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=programming-skills


def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


print(strStr(haystack="sadbutsad", needle="sad"))
print(strStr(haystack="leetcode", needle="leeto"))
print(strStr(haystack="mississippi", needle="issipi"))
