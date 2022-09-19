# Project Euler Problem 24
# Lexicographic Permutations

from itertools import permutations

n = 1000000
order = '0123456789'
perms = []

for i in permutations(order,len(order)):
    perms.append(''.join(i))

perms.sort()
print(perms[n-1])

