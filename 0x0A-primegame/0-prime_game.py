#!/usr/bin/python3
"""0.Prime Game
Given a set of consecutive integers starting from 1 up to and including n,
players take turns choosing a prime number from the set and removing that number
and its multiples from the set. The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    determines the winner of each round
    Return: the winner
    x: number of rounds they have to play
    nums: list of numbers
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        remove_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    if ben > maria:
        return "Ben"
    return None


def remove_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
