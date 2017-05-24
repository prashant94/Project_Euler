# Project Euler Problem 30
# Digit Fifth Powers

num_list = []
n = 2

def check_fifth_power(n):
    num = sum([int(i)**5 for i in str(n)])
    if num == n:
        return True
    return False

while n < 355000:
    if check_fifth_power(n):
        num_list.append(n)
    n += 1

print(sum(num_list))

