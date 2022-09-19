# Project Euler Problem 56
# Power Digit Sum

from itertools import product

maximum = 0
lst = [i for i in range(101)]

for i,j in product(lst,lst):
    powsum = sum([int(i) for i in str(i**j)])
    if powsum > maximum:
        maximum = powsum

print(maximum)



