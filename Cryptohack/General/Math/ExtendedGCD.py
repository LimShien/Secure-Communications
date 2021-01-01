"""
Using the two primes p = 26513, q = 32321, find the integers u,v such that

p * u + q * v = gcd(p,q)


Code referenced from https://www.techiedelight.com/extended-euclidean-algorithm-implementation/
"""

p = 26513
q = 32321

def xgcd(a, b):
    if a == 0:
        return (0, 1)
    else:
        x, y = xgcd(b % a, a)
        return (y - (b//a) * x, x)
 
x, y = xgcd(p,q)

print(x, y)
