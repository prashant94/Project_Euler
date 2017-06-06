# Project Euler Problem 49
# Prime Permutations

import numpy
from itertools import permutations

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

primes = list(primesfrom3to(9999))
primes = [i for i in primes if len(str(i)) >= 4]
answer = set()

for num in primes:
    num = [i for i in str(num)]
    perms = set()
    for j in permutations(num,len(num)):
        num2 = int(''.join(j))
        if num2 in primes:
            perms.add(num2)
    perms = sorted(perms)
    for i in range(len(perms)-2):
        if perms[i+1]-perms[i] == perms[i+2]-perms[i+1]:
            answer.add(perms[i])
            answer.add(perms[i+1])
            answer.add(perms[i+2])

answer = [str(i) for i in answer]
print(''.join(answer))
