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
    determines the winner of the game
    for given rounds and n values.
    Args:
        x(int): Number of rounds
        nums(list): List of n values for each round.

    Returns:
        Name of the player that won the most rounds (in string).
        If the winner cannot be determined, return None.
    """
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        maria_turn = True

        while n > 0:
            found_prime = False
            for j in range(2, n+1):
                if is_prime(j):
                    found_prime = True
                    n -= j
                    break
            if not found_prime:
                if maria_turn:
                    wins["Ben"] += 1
                else:
                    wins["Maria"] += 1
                break
            maria_turn = not maria_turn

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        if wins["Maria"] + wins["Ben"] == 0:
            return None
        else:
            return None
