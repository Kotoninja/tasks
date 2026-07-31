# import sys

# TLE solution
# def main():
#     n = int(input())
#     hash_map = {}

#     for i in range(n):
#         letter_count = int(input())
#         hash_map[chr(ord("a") + i)] = letter_count
#     # return hash_map

#     answer = 0

#     def get_length(letter):
#         nonlocal hash_map
#         if not hash_map[letter]:
#             hash_map.pop(letter)
#             return 0

#         next_key = chr(ord(letter) + 1)
#         # print(next_key)
#         if hash_map.get(next_key):
#             hash_map[letter] -= 1
#             if not hash_map[letter]:
#                 hash_map.pop(letter)
#             return 1 + get_length(next_key)
#         else:
#             hash_map[letter] -= 1
#             return 0

#     while hash_map:
#         inter_answer = 0
#         for i in hash_map.keys():
#             inter_answer += get_length(i)
#             break
#         answer += inter_answer
#         print(hash_map,answer)
#     return answer


# if __name__ == "__main__":
#     print(main())


import sys

def main():
    n = int(sys.stdin.readline())
    counts = [int(sys.stdin.readline()) for _ in range(n)]
    
    answer = 0
    for i in range(n - 1):
        answer += min(counts[i], counts[i+1])
    
    print(answer)

if __name__ == "__main__":
    main()