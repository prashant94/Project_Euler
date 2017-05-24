# Project Euler Problem 32
# Pandigital Products

from itertools import combinations

num_list = [1,2,3,4,5,6,7,8,9]
final = []
range_list = [i for i in range(1,2000)]

for a,b in combinations(range_list,2):
    prod = a*b
    a = [int(i) for i in str(a)]
    b = [int(i) for i in str(b)]
    prod2 = [int(i) for i in str(prod)]
    temp_list = a + b + prod2
    if sorted(temp_list) == num_list:
        final.append(prod)
        

print(sum(set(final)))     
    
    
