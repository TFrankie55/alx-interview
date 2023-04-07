#!/usr/bin/python3
'''Prime number game winner'''


def is_prime(num):
    """
    function to help check if a number is a prime
    """
    if num <= 3:
        return num > 1
    if num % 3 == 0 or num % 2 == 0 or num <= 1:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
        return True


def isWinner(x, nums):
    """
    To determine the winner of the game for each round and
    return the name of the player that won the most rounds.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for n in nums:
        if n > 0:
            found_prime = False
            for i in range(2, n+1):
                if is_prime(i):
                    found_prime = True
                    n -= i
                    break
            if not found_prime:
                if Maria:
                    Ben += 1
                else:
                    Maria += 1
                break
            Maria = not Maria

    if Ben > Maria:
        return 'Ben'
    elif Maria > Ben:
        return 'Maria'
    return None
