# Project Euler Problem 41
# Pandigital Prime

def check_prime(n):
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

def check_pandigit(n):
    num = [int(i) for i in str(n)]
    lst = [i for i in range(1,len(str(n))+1)]
    return sorted(num) == lst

#check divisibility by 3 for sum of digits of n digit numbers to get limits below

max_n = 10000000
min_n = 5000000
max_num = 0

for i in range(min_n,max_n):
    if check_prime(i) and check_pandigit(i):
        max_num = i

print(max_num)
    
