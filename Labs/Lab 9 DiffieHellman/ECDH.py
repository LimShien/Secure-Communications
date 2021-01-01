"""ECDH is now one of the most used key exchange methods, and uses the Diffie Hellman
method, but adds in elliptic curve methods. With this Alice generates (a) and Bob generates
(b). We select a point on a curve (G), and Alice generates aG, and Bob generates bG. They
pass the values to each other, and then Alice received bG, and Bob receives aG. Alice multiplies
by a, to get abG, and Bob will multiply by b, and also get abG. This will be their shared key.
D.1 Copy and paste the code from (you may have to run “pip install eccsnacks”):
& Web link (ECDH): https://asecuritysite.com/encryption/curve
and confirm that Bob and Alice will always get the same shared key


Do Bob and Alice end up with the same key?
    -yes
How large are the random numbers that Bob and Alice generate?
    -32 bytes
Do you think that this program will be secure? How might Eve discover the shared secret?
    -Man in the middle/Logjam attack

Estimate the time it would take her to discover the key if she can try one billion keys per
second:
    - ((2 ^^ 32 ) / 1000000))/ 60 = 71.59 minutes

How would you modify that program so that it was more secure?.
    - use of session key
"""
import os
import binascii

# Based on code from https://github.com/nnathan/eccsnacks/blob/master/eccsnacks/curve25519.py

P = 2 ** 255 - 19
A24 = 121665
def cswap(swap, x_2, x_3):
    dummy = swap * ((x_2 - x_3) % P)
    x_2 = x_2 - dummy
    x_2 %= P
    x_3 = x_3 + dummy
    x_3 %= P
    return (x_2, x_3)

def X25519(k, u):
    x_1 = u
    x_2 = 1
    z_2 = 0
    x_3 = u
    z_3 = 1
    swap = 0

    for t in reversed(range(255)):
        k_t = (k >> t) & 1
        swap ^= k_t
        x_2, x_3 = cswap(swap, x_2, x_3)
        z_2, z_3 = cswap(swap, z_2, z_3)
        swap = k_t

        A = x_2 + z_2
        A %= P

        AA = A * A
        AA %= P

        B = x_2 - z_2
        B %= P

        BB = B * B
        BB %= P

        E = AA - BB
        E %= P

        C = x_3 + z_3
        C %= P

        D = x_3 - z_3
        D %= P

        DA = D * A
        DA %= P

        CB = C * B
        CB %= P

        x_3 = ((DA + CB) % P)**2
        x_3 %= P

        z_3 = x_1 * (((DA - CB) % P)**2) % P
        z_3 %= P

        x_2 = AA * BB
        x_2 %= P

        z_2 = E * ((AA + (A24 * E) % P) % P)
        z_2 %= P

    x_2, x_3 = cswap(swap, x_2, x_3)
    z_2, z_3 = cswap(swap, z_2, z_3)

    return (x_2 * pow(z_2, P - 2, P)) % P
# When passed as a byte array
def unpack(s):
    if len(s) != 32:
        raise ValueError('Invalid Curve25519 scalar (len=%d)' % len(s))
    t = sum((s[i]) << (8 * i) for i in range(31))
    t += (((s[31]) & 0x7f) << 248)
    return t
# When passed as a string
def unpack2(s):
    if len(s) != 32:
        raise ValueError('Invalid Curve25519 scalar (len=%d)' % len(s))
    t = sum((ord(s[i]) ) << (8 * i) for i in range(31))
    t += (((ord(s[31]) ) & 0x7f) << 248)
    return t    

def pack(n):
    return ''.join([chr((n >> (8 * i)) & 255) for i in range(32)])

def clamp(n):
    n &= ~7
    n &= ~(128 << 8 * 31)
    n |= 64 << 8 * 31
    return n

def scalarmult(n, p):
    n = clamp(unpack(n))
    p = unpack2(p)
    return pack(X25519(n, p))

def scalarmult_base(n):
    n = clamp(unpack(n))
    return pack(X25519(n, 9))

a = os.urandom(32)
b = os.urandom(32)

a_pub = scalarmult_base(a)
b_pub = scalarmult_base(b)

k_ab = scalarmult(a, b_pub)
k_ba = scalarmult(b, a_pub)

print ("Bob private:\t",binascii.hexlify(a))
print ("Alice private:\t",binascii.hexlify(b))

print ("\n\nBob public:\t",binascii.hexlify(b_pub.encode()))
print ("Alice public:\t",binascii.hexlify(a_pub.encode()))

print ("\n\nBob shared:\t",binascii.hexlify(k_ba.encode()))
print ("Alice shared:\t",binascii.hexlify(k_ab.encode()))