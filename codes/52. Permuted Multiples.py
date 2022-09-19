# Project Euler Problem 52
# Permuted Multiples
# Slow Solution

from itertools import permutations

found = False
i = 10

while not found:
    num = [j for j in str(i)]
    perms = [int(''.join(j)) for j in permutations(num,len(num))]
    mults = []
    for x in range(2,7):
        mults.append(x*i)
    if all(mult in perms for mult in mults):
        print(i)
        found = True
    i += 1
