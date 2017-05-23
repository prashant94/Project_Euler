# Project Euler Problem 27
# Quadratic Primes

from math import sqrt, floor
from itertools import product

def check_prime(n):
    for i in range(2,floor(sqrt(abs(n)))):
        if n%i == 0:
            return False
    return True

a_list = [i for i in range(-999,1000)]
b_list = [i for i in range(-1000,1001)]
max_list = {}

for a,b in product(a_list,b_list):
    n = 0
    total = 0
    while(check_prime((n**2)+(a*n)+b)):
        total += 1
        n += 1
    max_list[total] = a*b

print(max_list[max(max_list)])
    
        
