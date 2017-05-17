# Project Euler Problem 21
# Amicable Numbers

from math import sqrt,ceil

n = 10000
total = 0

def sum_divisor(n):
    total = 0
    for i in range(1,ceil(n/2)+1):
        if n%i == 0:
            total += i
    return total

for a in range(n+1):
    b = sum_divisor(a)
    if b > a:
        if sum_divisor(b) == a:
            total += a+b
            
print(total)
