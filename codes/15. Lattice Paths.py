# Project Euler Problem 15
# Lattice Paths

import numpy as np

n = 20

def lattice_path_pascal(n):
    mat = np.zeros((n+1,n+1))
    for i in range(n+1):
        mat[0,i] = 1
        mat[i,0] = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            mat[i,j] = mat[i-1,j] + mat[i,j-1]
    return int(mat[n,n])

print(lattice_path_pascal(n))
    
