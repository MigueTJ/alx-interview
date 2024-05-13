#!/usr/bin/python3
'''
The Prime game - A game to find a winner using prime numbers
'''


def isWinner(x, nums):
    """
    Determines the winner of a game based on the number of prime numbers.

    Parameters:
    x (int): A number representing the total rounds of the game.
    nums (list): A list of numbers representing the maximum number
    in each round.

    Returns:
    Str: The name of the winner ('Maria' or 'Ben') or None if it's a draw.
    """

    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Initialize a list of boolean values representing prime numbers
    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False

    # Implement the Sieve of Eratosthenes to identify prime numbers
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i - 1]:
            for j in range(i * i, n + 1, i):
                primes[j - 1] = False

    # Count the primes for each round and update the players' scores
    for n in nums:
        primes_count = sum(primes[0:n])
        if primes_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    # Compare the scores and return the winner
    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return 'Maria'
    else:
        return 'Ben'
