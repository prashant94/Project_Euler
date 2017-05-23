# Project Euler Problem 28
# Number Spiral Diagonals

from math import ceil

n = 1001

bottom_right = [(4*(i**2))-(10*i)+7 for i in range(1,ceil(n/2)+1)]
top_right = [i**2 for i in range(1,n+1,2)]
bottom_left = [(4*(i**2))+1 for i in range(ceil(n/2))]
top_left = [(4*(i**2))-(6*i)+3 for i in range(1,ceil(n/2)+1)]

print(sum(bottom_right)+sum(top_right)+sum(bottom_left)+sum(top_left)-3)
