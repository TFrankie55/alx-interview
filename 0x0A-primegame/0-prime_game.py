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
Prime Number Game Winner


TOSIN OWOEYE
Help me with this code

Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins

Here's a possible implementation in Python:

python
Copy code
def is_prime(num):
    """
    Helper function to check if a number is prime
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determine the winner of the game for each round and return the name of the player that won the most rounds.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            # If n is 1, Ben wins automatically as there are no prime numbers for Maria to choose
            ben_wins += 1
            continue

        # Initialize a set to keep track of remaining numbers
        remaining = set(range(1, n + 1))

        # Maria starts the game
        maria_turn = True

        while True:
            # Find the next prime number
            prime = None
            for num in range(2, n + 1):
                if num in remaining and is_prime(num):
                    prime = num
                    break

            if prime is None:
                # If no prime number is found, the current player cannot make a move and loses
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            # Remove the prime number and its multiples from the set of remaining numbers
            for multiple in range(prime, n + 1, prime):
                remaining.discard(multiple)

            # Switch turn to the other player
            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
