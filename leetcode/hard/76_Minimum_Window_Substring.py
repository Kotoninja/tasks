# https://leetcode.com/problems/minimum-window-substring/description/


# NOT SOLVED
def minWindow(s: str, t: str) -> str:
    root_hash_map = {}

    for letter in t:
        root_hash_map[letter] = root_hash_map.get(letter, 0) + 1

    answer = ""
    indexes_hash_map: dict[str, list[int]] = {}

    l = 0

    while s[l] not in root_hash_map:
        l += 1

    r = l
    hash_map = root_hash_map.copy()

    n = len(s) - 1
    while r < n:
        if s[r] in root_hash_map:
            if (
                s[r] in indexes_hash_map
                and len(indexes_hash_map[s[r]]) == root_hash_map[s[r]]
            ):
                l = indexes_hash_map[s[r]].pop()
                indexes_hash_map[s[r]].append(r)
                hash_map[s[r]] = 1
            else:
                indexes_hash_map[s[r]] = indexes_hash_map.get(s[r], []) + [r]
                hash_map[s[r]] -= 1
                if not hash_map[s[r]]:
                    hash_map.pop(s[r])

            if not hash_map:
                answer = (
                    min(answer, s[l : r + 1], key=lambda x: len(x))
                    if answer
                    else s[l : r + 1]
                )

        r += 1
    return answer


print(minWindow(s="ADOBECODEBANC", t="ABC"))
# print(minWindow(s="ABABCBANC", t="ABC"))
# print(minWindow(s="ADOBBBECODEBANC", t="ABC"))
# print(minWindow(s="a", t="a"))
# print(minWindow(s="a", t="aa"))
# print(minWindow(s="ab", t="b"))
# print(minWindow(s="aaflslflsldkalskaaa", t="aaa"))
