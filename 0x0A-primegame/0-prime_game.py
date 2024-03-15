#!/usr/bin/python3
"Prime Numbe Games"


def isWinner(x, nums):
    """
    Determine the winner of each game played between Maria and Ben.

    Args:
        x (int): The number of rounds.
        nums (List[int]): An array of integerp.

    Returns:
        str: The name of the player that won the most rounds.
             If the winner cannot be determined, return None.

    Example:
        >>> print(isWinner(3, [4, 5, 1]))
        Ben
    """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime_count(num):
        count = 0
        for i in range(2, num + 1):
            if is_prime(i):
                count += 1
        return count

    winner_count = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        if prime_count(nums[i]) % 2 == 0:
            winner_count['Ben'] += 1
        else:
            winner_count['Maria'] += 1

    if winner_count['Maria'] > winner_count['Ben']:
        return 'Maria'
    elif winner_count['Maria'] < winner_count['Ben']:
        return 'Ben'
    else:
        return None
