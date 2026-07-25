"""
n - string length
m - count of operations

"""

# n, m = list(map(int, input().split()))
# s = input()

m = 6
s = "abacabadaba"
n = len(s)

mapping = {chr(ord("a") + i): chr(ord("a") + i) for i in range(26)}


for _ in range(n):
    n, m = input().split()

    for letter, value in mapping:
        if mapping[letter] == n:
            mapping[letter] = m
        elif mapping[letter] == m:
            mapping[letter] = n

result = "".join(mapping[char] for char in s)

print(result)
