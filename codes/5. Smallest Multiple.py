# Project Euler Problem 5 
# Smallest Multiple

from functools import reduce

def gcd(*numbers):
    from fractions import gcd
    return reduce(gcd, numbers)

def lcm(nums):
    numbers = []
    for num in nums:
        numbers.append(num)
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return reduce(lcm, numbers, 1)

nums = []
for i in range(1,21):
    nums.append(i)

print(lcm(nums))
    
