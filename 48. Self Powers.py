# Project Euler Problem 48
# Self Powers

total = 0

for i in range(1,1001):
    total += i**i

print(str(total)[-10:])
