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
    maria_win = 0
    ben_win = 0

    for n in nums:
        if n == 1:
            """
            If n is 1, Ben wins as there are
            no prime numbers for Maria to choose
            """
            ben_win += 1
            continue

        # Initialize a set to keep track of remaining numbers
        remaining = set(range(1, n + 1))

        # This time, Maria starts the game
        maria_turn = True

        while True:
            # To find the next prime number
            prime = None
            for num in range(2, n + 1):
                if num in remaining and is_prime(num):
                    prime = num
                    break

            if prime is None:
                """
                If no prime number is found, the
                current player cannot make a move and loses
                """
                if maria_turn:
                    ben_win += 1
                else:
                    maria_win += 1
                break

            """
            To remove the prime number and its multiples
            from the set of remaining numbers
            """
            for multiple in range(prime, n + 1, prime):
                remaining.discard(multiple)

            # Switch to the other player's turn
            maria_turn = not maria_turn

    if maria_win > ben_win:
        return "Maria"
    elif ben_win > maria_win:
        return "Ben"
    else:
        return None
