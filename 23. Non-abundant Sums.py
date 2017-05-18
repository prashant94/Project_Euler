# Project Euler Problem 23
# Non-abundant Sums

from math import ceil
from itertools import product

n = 28123

def sum_divisor(n):
    total = 0
    for i in range(1,ceil(n/2)+1):
        if n%i == 0:
            total += i
    return total

def is_abundant(n):
    return sum_divisor(n) > n


num_list = {i: i for i in range(1,n)}
abundant_list = [i for i in range(1,n+1) if is_abundant(i)]

for a,b in product(abundant_list,abundant_list):
    try:
        if a+b < n:
            del num_list[a+b]
    except:
        continue

print(sum(num_list))
