#!/usr/bin/python3

''' This module contains the functions sieve_of_eratosthenis() and
    isWinner() '''


def sieve_of_eratosthenes(n):
    ''' Gets all prime numbers upto and including n(if n is prime) '''

    prime = [True for i in range(n + 1)]
    primes = []
    p = 2

    while p * p <= n:
        if prime[p] is True:

            # Remove all multiples of p from consideration
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all the prime numbers
    for p in range(2, n + 1):
        # If it is not changed to False, it is prime
        if prime[p]:
            primes.append(p)
    return primes


def isWinner(x, nums):
    ''' Returns either Maria or Ben depending on who has more wins '''
    players = [{"name": "Maria", "wins": 0}, {"name": "Ben", "wins": 0}]

    for round in range(x):
        n = nums[round]
        # All the unused primes that are less than n
        primes = sieve_of_eratosthenes(n)
        # All the numbers that are less than n
        all_numbers = [num for num in range(1, n + 1)]

        # prime index
        i = 0
        for player in players:
            # The first available prime number in the list of primes
            if primes == []:
                break

            prime = primes[i]

            for number in all_numbers:
                # Player takes out the prime and all multiples of the prime
                if number == prime or number % prime == 0:
                    all_numbers.remove(number)

            if i < len(primes) - 1:
                i += 1

            # If there are no more prime numbers left to play, the round ends
            else:
                # If the round ended on Ben's turn
                if player["name"] == "Maria":
                    # Maria gets a point
                    players[0]["wins"] += 1

                else:
                    # Otherwise Ben gets a point
                    players[1]["wins"] += 1
                break

    if players[0]["wins"] > players[1]["wins"]:
        return "Maria"
        # elif players[0]["wins"] < players[1]["wins"]:
        # return "Ben"
    else:
        return "Ben"
