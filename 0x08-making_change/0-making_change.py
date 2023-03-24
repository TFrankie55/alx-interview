#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rem > 0:
        if coin_idx >= n:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count


'''def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any
        number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    maxi = coins[1]
    x = 0
    coins.pop(0)
    rem = total % maxi
    if rem == 0:
        return total / maxi
    quot = total // maxi
    while x < len(coins):
        remc = rem % coins[x]
        if remc == 0:
            return quot + (rem // coins[x])
        if x == 0:
            return -1
        quotc = rem // coins[x]
        rem = remc
        quot += quotc
        x += 1
    return quot'''
