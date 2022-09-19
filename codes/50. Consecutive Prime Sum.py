# Project Euler Problem 50
# Consecutive Prime Sum

import numpy
from math import *

def primesfrom3to(n):
    sieve = numpy.ones(int(n/2), dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::int(i)] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

n = 1000000
primes_under_million = [2] + list(primesfrom3to(n))

nsum = 1
n = 1
while nsum < 10**6:
    nsum = 0.5*(n**2)*(log(n, e))
    n += 1

primes_subset = primes_under_million[:n]
nsum = sum(primes_under_million[:n])
while nsum > 10**6:
    n -= 1
    nsum = sum(primes_under_million[:n])
primes_sum = 0
index = 0
for i in range(len(primes_subset)):
    if i % 2 == 1:
        pass
    else:
        sumprimes = sum(primes_subset[:i])
        if sumprimes > primes_sum and sumprimes < 10**6 and sumprimes in primes_under_million:
            primes_sum = sumprimes
            index = i

j = index + 1
start = 0
while j <= n:
    while (j-start) >= (n-index):
        sumprimes = sum(primes_subset[start:j])
        if sumprimes > primes_sum and sumprimes in primes_under_million:
            primes_sum = sumprimes
        start += 1
    j += 1
    start = 0
print(primes_sum)
