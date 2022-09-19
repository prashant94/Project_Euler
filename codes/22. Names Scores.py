# Project Euler Problem 22
# Names Scores

with open('p022_names.txt', 'r') as f:
    names = f.read()

names = names.split(',')
names = [i.replace('"','') for i in names]
names = [i.lower() for i in names]
names.sort()
total = 0

for i in range(1,len(names)+1):
    curr_name = sum([ord(i)-96 for i in names[i-1]])
    total += curr_name*i

print(total)
    
    
