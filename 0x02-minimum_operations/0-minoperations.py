#!/usr/bin/python3

''' Contanins the function prime_factors, minOperations '''


def prime_factors(n):
    ''' Find out if a number is prime '''
    factors = []
    for i in range(2,  int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def minOperations(n):
    ''' Whatever you day big dog '''
    if not isinstance(n, int) or n <= 1:
        return 0

    return sum(prime_factors(n))
