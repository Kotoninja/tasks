# https://leetcode.com/problems/product-of-array-except-self/description/


def productExceptSelf(nums: list[int]) -> list[int]:
    # brute force solution O(n^2)
    # result: list[int] = []

    # for i in range(len(nums)):
    #     calculation = 1
    #     for j in range(len(nums)):
    #         if i == j:
    #             continue
    #         calculation *= nums[j]
    #     result.append(calculation)

    # return result

    # divisino solution
    # max_number = 1
    # zero_count = 0

    # for number in nums:
    #     if not number:
    #         zero_count += 1
    #     else:
    #         max_number *= number

    # result: list[int] = []

    # for number in nums:
    #     if not number:
    #         if zero_count == 1:
    #             result.append(max_number)
    #         else:
    #             result.append(0)
    #     else:
    #         if zero_count:
    #             result.append(0)
    #         else:
    #             result.append(int(max_number / number))

    # return result

    # O(n)
    # prefix = []
    # n = len(nums)

    # for index, number in enumerate(nums):
    #     if not prefix:
    #         prefix.append(number)
    #     else:
    #         prefix.append(prefix[index - 1] * number)

    # postfix = []

    # for index, number in enumerate(nums[::-1]):
    #     if not postfix:
    #         postfix.append(number)
    #     else:
    #         postfix.append(postfix[index - 1] * number)

    # postfix = postfix[::-1]

    # result: list[int] = []
    # for i in range(n):
    #     if not i:
    #         result.append(postfix[i + 1])
    #     elif i == n - 1:
    #         result.append(prefix[i - 1])
    #     else:
    #         result.append(prefix[i - 1] * postfix[i + 1])

    # return result

    # O(n) and O(1)

    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(n - 1, -1, -1):
        result[j] *= postfix
        postfix *= nums[j]

    return result


print(productExceptSelf(nums=[1, 2, 3, 4]))
print(productExceptSelf(nums=[2, 2, 2, 2]))
print(productExceptSelf(nums=[0, 0]))
print(productExceptSelf(nums=[-1, 1, 0, -3, 3]))
