# Project Euler Problem 47
# Distinct Primes Factors

def primefac(n):
    primfac = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.add(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.add(n)
    return primfac


def answer():
   i = 1
   while True:
       i += 1
       if len(primefac(i)) == 4 and len(primefac(i+1)) ==4 and len(primefac(i+2)) == 4 and len(primefac(i+3)) == 4:
           return i

print(answer())
