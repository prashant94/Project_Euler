# Project Euler Problem 36
# Double-base Palindromes

n = 1000000
num_list = []

def palindrome(num):
    return str(num) == str(num)[::-1]

def check_db_palindrome(n):
    return palindrome(n) and palindrome(str(bin(n)[2:]))

for i in range(n):
    if check_db_palindrome(i):
        num_list.append(i)

print(sum(num_list))
