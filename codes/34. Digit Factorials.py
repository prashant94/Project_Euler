# Project Euler Problem 34
# Digit Factorials

def fact(n):
    factorial = 1
    for i in range(n,0,-1):
        factorial *= i
    return factorial

def fact_sum(n):
    num_sum = [int(i) for i in str(n)]
    if sum([fact(i) for i in num_sum]) == n:
        return True
    return False

factorials = []

for i in range(3,fact(9)):
    if fact_sum(i):
        factorials.append(i)

print(sum(factorials))
