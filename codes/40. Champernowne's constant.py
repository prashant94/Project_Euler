# Project Euler Problem 40
# Champernowne's constant

n = 1000000
num = ''

for i in range(1,n+1):
    num = num + str(i)

print(int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999]))
