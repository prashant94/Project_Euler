# Project Euler Problem 37
# Truncatable Primes

from math import sqrt, ceil

num_list = []
x = 11

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

while len(num_list) != 11:
    num = x
    num = [i for i in str(num)]
    front_remove = list(num)
    back_remove = list(num)
    perms = []
    while len(front_remove) != 0:
        perms.append(int(''.join(front_remove)))
        perms.append(int(''.join(back_remove)))
        front_remove.pop(0)
        back_remove.pop()
    if all(isprime(w) for w in perms):
        num_list.append(x)
    x += 1
    
print(sum(num_list)) 
