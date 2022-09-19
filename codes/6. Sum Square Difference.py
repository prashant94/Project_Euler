# Project Euler Problem 6
# Sum Square Difference

sum_of_squares = 0
square_of_sum = 0

for i in range(101):
    sum_of_squares += i**2
    square_of_sum += i

print(square_of_sum**2 - sum_of_squares)
