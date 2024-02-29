#!/usr/bin/python3
"""
determine the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (List[int]): List of the values of the coins in your possession.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total. Returns -1 if total cannot be met.

    Example:
        >>> makeChange([1, 2, 25], 37)
        7
        >>> makeChange([1256, 54, 48, 16, 102], 1453)
        -1
    """
    if total <= 0:
        return 0

    # Initialize a list to store the fewest number of coins needed for each total amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update the dp array with the fewest number of coins needed for each total amount
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
