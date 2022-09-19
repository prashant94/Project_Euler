# Project Euler Problem 38
# Pandigital Multiples

def create_concat(n):
    con = []
    i = 1
    while len(''.join(con)) < 9:
        temp = n*i
        con.append(str(temp))
        i += 1
    return ''.join(con)
        
max_num = 0
n = 9999
check = [str(i) for i in range(1,10)]

for i in range(1,n):
    concat = create_concat(i)
    
    concat2 = [str(i) for i in concat]
    
    if sorted(concat2) == check and int(concat) > max_num:
        max_num = int(concat)

print(max_num)
