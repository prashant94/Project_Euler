# Project Euler Problem 35
# Circular Primes

from math import sqrt,ceil
from itertools import permutations

n = 1000000
total = 0

def check_prime(n):
    for i in range(2,ceil(sqrt(n))):
        if n%i == 0:
            return False
    return True
    
for i in range(11,n):
    num = [a for a in str(i)]
    perms = []
    for j in range(len(num)):
        num.append(num.pop(0))
        perms.append(int(''.join(num)))
    if all(check_prime(w) for w in perms):
        total += 1
    
print(total+4)
