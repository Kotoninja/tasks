import math

n = list(map(int, input().split()))
k = int(input())

result = 0

for i in range(len(n)):
    for j in range(len(n), i, -1):
        if len(n[i:j]) != len(n) and math.prod(n[i:j]) < k:
            result += 1

print(result)
