# Project Euler Problem 46
# Goldbach's Other Conjecture

import numpy
from math import sqrt,ceil

def primesfrom3to(n):
    sieve = numpy.ones(int(n/2), dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::int(i)] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def check_prime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def goldbach(n):
    primes = primesfrom3to(n-1)
    primes = [2] + list(primes)
    for i in range(1,ceil(sqrt(n))):
        for j in primes:
            if n == j + (2*(i**2)):
                return True
    return False
        
def answer():
    i = 1
    while True:
        i += 2
        if check_prime(i):
            continue
        else:
            if not goldbach(i):
                return i

print(answer())
        
