# Project Euler Problem 2
# Even Fibonacci Numbers

total = 0

fib = [1,2]

while (fib[-1] < 4000000):
    if (fib[-1]%2 == 0):
        total += fib[-1]
    temp = fib[-1]
    fib[-1] += fib[0]
    fib[0] = temp
    
print(total)
