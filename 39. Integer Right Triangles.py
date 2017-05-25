# Project Euler Problem 39
# Integer Right Triangles

max_p, max_val = 0, 0

for p in range(1,1000):
    total_sols = 0
    for a in range(2,int(p/2)):
        if (p*(p-(2*a))) % (2*(p-a)) == 0:
            total_sols += 1
        if total_sols > max_val:
            max_p = p
            max_val = total_sols

print(max_p)

