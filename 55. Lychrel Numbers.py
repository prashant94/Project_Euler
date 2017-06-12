# Project Euler Problem 55
# Lychrel Numbers

n = 10000
i = 0
total = 0

def palindrome(num):
    return str(num) == str(num)[::-1]

while i < n:
    num = i
    for j in range(1,51):
        temp = int(str(num))+int(str(num)[::-1])
        if palindrome(temp):
            total += 1
            break
        num = temp
    i += 1

print(n-total)
        
