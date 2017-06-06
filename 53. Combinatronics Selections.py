# Project Euler Problem 53
# Combinatronics Selections

from math import ceil

def fact(n):
    factorial = 1
    for i in range(n,0,-1):
        factorial *= i
    return factorial

def ncr(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))

n = 1000000
total = 0

for i in range(1,101):
    for j in range(1,i):
        if ncr(i,j) > n:
            total += 1

print(total)
        
