# Project Euler Problem 9
# Special Pythagorean Triplet

from itertools import combinations

lst = []
n = 1000

for a,b in combinations(range(1,n+1),2):
    c = n-a-b
    if (a + b + c ==1000):
        lst.append((a,b,c))


for i in lst:
    if (i[0]**2 + i[1]**2 == i[2]**2):
        print(i[0]*i[1]*i[2])
    
