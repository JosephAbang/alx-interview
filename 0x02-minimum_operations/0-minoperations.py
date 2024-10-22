#!/usr/bin/python3

"""
    Function to calculate minimum operations
"""


def minOperations(n):
    """
    Determines the minimum number of operations needed to reach `n` characters.

    Args:
    n (int): The target number of characters.

    Returns:
    int: The minimum number of operations.
    """
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
