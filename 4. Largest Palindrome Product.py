# Project Euler Problem 4 
# Largest Palindrome Product



def palindrome(num):
    return str(num) == str(num)[::-1]

largest = 0

for i in range(100,999):
    for j in range(100,999):
        if (palindrome(i*j) and i*j > largest):
            largest = i*j
        
print(largest)
