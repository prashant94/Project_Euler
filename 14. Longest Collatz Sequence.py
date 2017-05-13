# Project Euler Problem 14
# Longest Collatz Sequence
# Very very inefficient solution

num = 1000000
largest_seq = 0
largest_num = 0

def collatz(n):
    count = 0
    while (n > 1):
        if (n%2 == 0):
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    return count+1

for i in range(num):
    if (collatz(i) > largest_seq):
        largest_seq = collatz(i)
        largest_num = i

print(largest_num)
