#!/usr/bin/python3

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
