# Project Euler Problem 3
# Largest Prime Factors

from math import sqrt,ceil

num = 600851475143

largest = 0

while (num%2 == 0):
    num /= 2

for i in range(3, ceil(sqrt(num)), 2):
    while (num%i == 0):
        num /= i
        largest = i
        
print(largest)
