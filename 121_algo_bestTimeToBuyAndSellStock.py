# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction 
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.



# o(n^2)
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit


# one pass
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    min_value = float('inf')
    for i in range(len(prices)):
        if prices[i] < min_value:
            min_value = prices[i]
        elif prices[i] - min_value > max_profit:
            max_profit = prices[i] - min_value
       
    return max_profit



prices = [7,1,5,3,6,4] # 5
print maxProfit(prices)
    





