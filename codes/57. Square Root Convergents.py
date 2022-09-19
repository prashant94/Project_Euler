# Project Euler Problem 57
# Square Root Conversgents

def findrootn(n):
    return 1+(1/(2 + findrootn(n-1)))
