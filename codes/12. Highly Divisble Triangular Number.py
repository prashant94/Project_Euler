# Project Euler Problem 12
# Highly Divisible Triangular Number

from math import sqrt, ceil
from functools import reduce

nat_num = 1
triangular = 0
ans = 0
fact = []

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
while (len(fact) < 500):
    triangular = (nat_num*(nat_num+1))/2
    fact = factors(triangular)
    nat_num += 1    
                   
print(triangular)
