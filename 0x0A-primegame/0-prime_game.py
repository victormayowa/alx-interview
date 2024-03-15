#!/usr/bin/python3
"Prime Numbe Games"


def is_prime(num):
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """
    Get all prime numbers up to n.
    """
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def can_win(nums):
    """
    Check if a player can win the game for a given set of numbers.
    """
    primes = get_primes(max(nums))
    total_primes = len(primes)
    moves = [0] * (total_primes + 1)
    for num in nums:
        for i in range(total_primes):
            if primes[i] <= num:
                moves[i] += 1
    xor = 0
    for move in moves:
        xor ^= move
    return xor != 0


def isWinner(x, nums):
    """
    Determine the winner of the game.
    """
    maria_wins = 0
    ben_wins = 0
    for num in nums:
        if can_win(range(1, num + 1)):
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
