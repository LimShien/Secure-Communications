"""
First, pick two prime numbers:
p=3
q=7
Now calculate N (p.q) and PHI [(p-1).(q-1)]:
N= 21
PHI = 12
Now pick a value of ewhich does not share a factor with PHI [gcd(PHI,e)=1]: 
e=11
Now select a value of d, so that (e.d) (mod PHI) = 1:[Note: You can use this page to find d: https://asecuritysite.com/encryption/inversemod]
d=
Now for a message of M=5, calculate the cipher as:C = Me(mod N) = Now decrypt your ciphertext with:M = Cd(mod N) =Did you get the value of your message back (M=5)? If not, you have made a mistake, so go back and check

"""
from Crypto.PublicKey import RSA
p=11 
q=3
N=p*q
PHI=(p-1)*(q-1)
e=3
for d in range(1,100):
    if ((e*d % PHI)==1): break
print (e,N)
print (d,N)
M=4
cipher = M**e % N
print (cipher)
message = cipher**d % N
print(message)

"""
E.2 in the RSA method, we have a value of e, and then determine d from (d.e) (mod PHI)=1. Buthow do we use code to determine d? Wellwe can use the Euclidean algorithm. The code for this is givenat:https://asecuritysite.com/encryption/inversemodUsing the code, can youdetermine the following:

Inverseof 53 (mod 120)= 77
Inverseof 65537 (mod 1034776851837418226012406113933120080)=24824613312450973485395773715904353
"""

def extended_euclidean_algorithm(a, b):
    """
    Returns a three-tuple (gcd, x, y) such that
    a * x + b * y == gcd, where gcd is the greatest
    common divisor of a and b.

    This function implements the extended Euclidean
    algorithm and runs in O(log b) in the worst case.
    """
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    """
    Returns the multiplicative inverse of
    n modulo p.

    This function returns an integer m such that
    (n * m) % p == 1.
    """
    gcd, x, y = extended_euclidean_algorithm(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        # Either n is 0, or p is not a prime number.
        raise ValueError(
            '{} has no multiplicative inverse '
            'modulo {}'.format(n, p))
    else:
        return x % p

print("getting d value:")
print(inverse_of(e, PHI))

"""
Run the following code and observe the output of the keys. If you now change the key generation key from ‘PEM’to ‘DER’, how does the output change

--output in bytes format after changing to DER from PEM
"""

key = RSA.generate(2048)
binPrivKey = key.exportKey('DER')
binPubKey =  key.publickey().exportKey('DER')
print (binPrivKey)
print(binPubKey)