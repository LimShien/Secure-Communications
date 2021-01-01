"""
There are many tools to calculate the GCD of two integers, but for this task we recommend looking up Euclid's Algorithm.

Try coding it up; it's only a couple of lines. Use a = 12, b = 8 to test it.

Now calculate gcd(a,b) for a = 66528, b = 52920 and enter it below. 
"""
a = 12
b = 8

def gcd(a, b):
    if b != 0:
        c = a - b
        while (c > b):
            c = c - b
        a = b
        b = c
        gcd(a, b)
    else:
        print(a)

gcd(66528, 52920)