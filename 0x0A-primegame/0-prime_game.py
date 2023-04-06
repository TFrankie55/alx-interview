#!/usr/bin/python3
'''Prime number game winner'''


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


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
    """
    dict to keep track of wins for each player
    """

    for n in nums:
        maria_turn = True
        """
        line to keep track of Maria's turn
        """

        while n > 0:
            found_prime = False
            """
            if a prime number is found in the set
            """
            for j in range(2, n+1):
                if is_prime(j):
                    found_prime = True
                    n -= j
                    break
            if not found_prime:
                """
                if no prime number is found, current player loses
                """
                if maria_turn:
                    wins["Ben"] += 1
                else:
                    wins["Maria"] += 1
                break
            maria_turn = not maria_turn
            """
            switch btw Maria and Ben turn
            """

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        if wins["Maria"] + wins["Ben"] == 0:
            return None
        else:
            return None
