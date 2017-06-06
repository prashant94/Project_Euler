# Project Euler Problem 45
# Triangular, Pentagonal, And Hexagonal

from math import sqrt

# All hexagonal nums are subset of triangular nums, so no need to check triangulars
def ispentagonal(n):
    num = (sqrt(24*n+1)+1)/6
    return num.is_integer()

def answer():
    i = 143
    while True:
        i += 1
        hexa = int(2*i*i - i)
        if ispentagonal(hexa):
            return hexa

print(answer())
