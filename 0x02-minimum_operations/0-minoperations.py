#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
    """This loop finds all the factors
    of n and increments the number of
    operations for each factor"""
        while n % i == 0:
            operations += i
            n /= i
        i += 1
    return operations + n
