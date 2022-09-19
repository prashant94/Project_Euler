# Project Euler Problem 7
# 10001st Prime

import numpy
def primesfrom3to(n):
    sieve = numpy.ones(int(n/2), dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::int(i)] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

sieve = [2] + list(primesfrom3to(105000))


print(sieve[10000])
