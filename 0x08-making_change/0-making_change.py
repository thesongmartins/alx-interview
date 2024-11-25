#!/usr/bin/python3
"""
Making changes
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    needed to meet a given amount
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
