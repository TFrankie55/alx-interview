#!/usr/bin/python3


def is_prime(num):
    """
    function to help check if a number is a prime
    """
    if num <= 3:
        return True
    if num <= 1:
        return False
    if num % 3 == 0 or num % 2 == 0:
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
    ''' dict to keep track of wins for each player '''

    for n in nums:
        maria_turn = True  # line to keep track of Maria's turn

        while n > 0:
            found_prime = False  # if a prime number is found in the set
            for j in range(2, n+1):
                if is_prime(j):
                    found_prime = True
                    n -= j
                    break
                if not found_prime:
                    # if no prime number is found, current player loses
                    if maria_turn:
                        wins["Ben"] += 1
                    else:
                        wins["Maria"] += 1
                    break
                maria_turn = not maria_turn  # switch btw Maria and Ben turn

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
