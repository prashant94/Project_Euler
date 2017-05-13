# Project Euler Problem 10
# Sum of Primes

import numpy

n = 2000000
total = 0

def primesfrom3to(n):
    sieve = numpy.ones(int(n/2), dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::int(i)] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

sieve = [2] + list(primesfrom3to(n))

for i in sieve:
    total += i

print(total)
