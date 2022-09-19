# Project Euler Problem 25
# 1000-Digit Fibonacci Number

fib = [1,1]
index = 2

while (len(str(fib[-1])) < 1000):
    fib.append(fib[-1]+fib[-2])
    index += 1

print(index)

