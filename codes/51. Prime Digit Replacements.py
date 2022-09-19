# Project Euler Problem 51
# Prime Digit Replacements

import numpy

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

def eight_prime_family(prime, rd):
    c=0
    for digit in '0123456789':
        n = int(prime.replace(rd, digit))
        if (n>100000 and check_prime(n)):
            c=c+1
    return c==8
 
for prime in primesfrom3to(1000000):
    if (prime>100000):
        s = str(prime)
        last_digit = s[5:6]
        if (s.count('0')==3 and eight_prime_family(s,'0') \
         or s.count('1')==3 and last_digit != '1' and eight_prime_family(s,'1') \
         or s.count('2')==3 and eight_prime_family(s,'2')):
             print(s)
    
    
