"""We can determine the values of g which will work for a given prime number with the
following:

Run the program and determine the possible g values for these prime numbers:
p=11:2
p=41:6
On the Internet, find a large prime number, and determine the values of g that are possible:
p=5659  , g = 2

"""

import sys
import random
p = 5659 

def getG(p):
    for x in range(1, p):
        rand = x
        exp = 1
        next = rand % p

        while (next != 1):
            next = (next*rand) % p
            exp = exp+1
        if (exp == p-1):
            return rand

print(getG(p))
