#!/usr/bin/python3

''' Contanins the function isPrime, find_prime_factors, factorize_add_primes,
    minOperations '''


def prime(n):
    ''' Find out if a number is prime '''
    for i in range(2,  int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

''' Big man ting '''

def minOperations(n):
    ''' Whatever you day big dog '''
    if not isinstance(n, int) or n <= 1:
        return 0

    # Function to find prime factors using the Sieve of Eratosthenes
    def prime_factors(n):
        ''' We prime baby '''
        factors = []
        for i in range(2, int(n**0.5) + 1):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 1:
            factors.append(n)
        return factors

    factors = prime_factors(n)
    return sum(factors)


def find_prime_factors(n):
    ''' Find all the prime factors of n '''
    return [i for i in range(2, n + 1) if is_prime(i) and n % i == 0]


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
    # print(primes)

    min_ops = factorize_add_primes(n, primes, 0)

    return min_ops
