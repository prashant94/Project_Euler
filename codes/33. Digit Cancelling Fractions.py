# Project Euler Problem 33
# Digit Cancelling Fractions

from fractions import Fraction
from functools import reduce
import operator

frac_list = []

def removeCommon(a, b):
    for e in a[:]:
        if e in b:
            a.remove(e)
            b.remove(e)

for b in range(10,100):
    for a in range(10,b):
        p = [i for i in str(a)]
        q = [i for i in str(b)]
        if '0' in p or '0' in q:
            continue
        removeCommon(p,q)
        if not p or not q:
            continue
        p = int(''.join(p))
        q = int(''.join(q))
        if p == a and q == b:
            continue
        try:
            if Fraction(a,b) == Fraction(p,q):
                frac_list.append(Fraction(a,b))
        except:
            pass


lowest = reduce(operator.mul, frac_list, 1)
print(lowest.denominator)
        
        
        
