# Project Euler Problem 42
# Coded Triangle Numbers

with open('p042_words.txt', 'r') as f:
    words = f.read()
    words = words.split(',')
    words = [word[1:-1] for word in words]
    words = [i.lower() for i in words]
    longest = max(words, key=len)

def calc_sum(s):
    total = sum([ord(i)-96 for i in s])
    return total

total = 0
tri_nums = []
temp_tri = 1
new_num = 0

while new_num < calc_sum(longest):
    new_num = 0.5*temp_tri*(temp_tri+1)
    tri_nums.append(int(new_num))
    temp_tri += 1

for word in words:
    if calc_sum(word) in tri_nums:
        total += 1
        
print(total)




