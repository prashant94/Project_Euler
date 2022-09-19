# Project Euler Problem 29
# Distinct Powers

from itertools import product

order_list = []
a_list = [i for i in range(2,101)]

for a,b in product(a_list,a_list):
    order_list.append(a**b)

print(len(set(order_list)))
