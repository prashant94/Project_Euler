# Project Euler Problem 20
# Factorial Digit Sum

def fact(n):
    factorial = 1
    for i in range(n,0,-1):
        factorial *= i
    return factorial   

num = fact(100)
num = [int(i) for i in str(num)]
print(sum(num))
