#!/usr/bin/python3
"""
Prime number game winner
"""


def primes(n):
    """
    function to help check if a number is a prime
    """
    primes_list = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            primes_list.append(p)
            for j in range(p, n + 1, p):
                sieve[j] = False
    return primes_list


def isWinner(x, nums):
    """
    To determine the winner of the game for each round and
    return the name of the player that won the most rounds.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for j in range(x):
        primes_list = primes(nums[j])
        if len(primes_list) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
