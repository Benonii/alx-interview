#!/usr/bin/python3

''' Contanins the function isPrime, find_prime_factors, factorize_add_primes,
    minOperations '''


def is_prime(n):
    ''' Find out if a number is prime '''
    for i in range(2,  (n // 2) + 1):
        if n % i == 0:
            return False
    return True


def find_prime_factors(n):
    ''' Find all the prime factors of n '''
    return [i for i in range(2, n) if is_prime(i) and n % i == 0]


def factorize_add_primes(n, primes, Sum):
    ''' Find the sum of the prime factors of n '''
    for i in primes:
        if n / i == 1.0:
            Sum += i
            return Sum
        elif n % i == 0:
            Sum += i
            return factorize_add_primes(n / i, primes, Sum)
    return Sum


def minOperations(n):
    ''' Function to determine the miminum operations required to print a
        character n times wit copyAll and paste as the only operations. '''
    if not isinstance(n, int) or n <= 1:
        return 0
    primes = find_prime_factors(n)

    min_ops = factorize_add_primes(n, primes, 0)

    return min_ops