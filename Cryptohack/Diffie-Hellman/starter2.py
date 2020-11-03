"""
Every element of a finite field Fp can be used to make a subgroup H under repeated action of multiplication. In other words, for an element g: H = {g, g^2, g^3, ...}

A primitive element of Fp is an element whose subgroup H = Fp, i.e., every element of Fp, can be written as g^n mod p for some integer n. Because of this, primitive elements are sometimes called generators of the finite field.

For the finite field with p = 28151 find the smallest element g which is a primitive element of Fp.
"""

p = 28151
g = 1
found = False
#g*n mod p

while not found:
    for x in range(2, p):
        if(pow(g, x, p) == g):
            break
        if x > p-2:
            found = True
    if found:
        print(g)
    else:
        g +=1