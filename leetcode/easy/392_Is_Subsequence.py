# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75


def isSubsequence(s: str, t: str) -> bool:
    sl = 0
    sr = len(s) - 1

    tl, tr = 0, len(t) - 1

    if not s:
        return True

    while tl <= tr:
        if t[tl] == s[sl] and tr != tl:
            tl += 1
            sl += 1
        else:
            tl += 1

        if t[tr] == s[sr]:
            tr -= 1
            sr -= 1
        else:
            tr -= 1
        if sl > sr:
            return True
    return False


# print(isSubsequence(s="abc", t="ahbgdc"))
# print(isSubsequence(s="axc", t="ahbgdc"))
# print(isSubsequence(s="aza", t="abzba"))
# print(isSubsequence(s="abbc", t="ahbdc"))
# print(isSubsequence(s = "abc", t = "ahbgdc"))
