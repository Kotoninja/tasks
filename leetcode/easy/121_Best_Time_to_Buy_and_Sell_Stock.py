# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


def maxProfit(prices: list[int]) -> int:
    answer = 0

    l, r = 0, 0

    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        else:
            answer = max(prices[r] - prices[l], answer)
        r += 1
    return answer


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(maxProfit(prices=[7, 6, 4, 3, 1]))
print(maxProfit(prices=[1]))
# print(maxProfit())
