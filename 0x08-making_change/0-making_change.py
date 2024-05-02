#!/usr/bin/python3
"""
This module contains a function that calculates the fewest number of coins
needed to meet a given amount total using a greedy programming approach.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total >= coin:
            coin_count += total // coin
            total %= coin
        if total == 0:
            return coin_count
    return -1 if total != 0 else coin_count
