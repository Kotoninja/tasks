# https://leetcode.com/problems/group-anagrams/description/


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    result_dict: dict = {}

    for word in strs:
        inter_dict: dict = {}
        for letter in word:
            inter_dict[letter] = inter_dict.get(letter, 0) + 1

        # Next iteration
        key = frozenset(inter_dict.items())
        result_dict[key] = result_dict.get(key, []) + [word]

    return list(result_dict.values())


print(groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
