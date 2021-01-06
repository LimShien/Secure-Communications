"""

I need to produce millions of RSA keys quickly and the standard way just doesn't cut it. Here's yet another fast way to generate primes which has actually resisted years of review.
"""
import math
import random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes
from gmpy2 import is_prime


ct ="249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28"
with open('/home/kali/College/Secure-Communications/Cryptohack/RSA/Primes Part2/FastPrimes/key.pem') as f:
    key = RSA.importKey(f.read())
##Retrieve the value from RSA KEY PAIR 
n = key.n  
e = key.e 
#factor DB 
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161

phi = (p-1)*(q-1)
d = inverse(e, phi) 


with open('/home/kali/College/Secure-Communications/Cryptohack/RSA/Primes Part2/FastPrimes/pk.pem') as f:
    pk = RSA.importKey(f.read())

#####cant continue because cant generate RSA private key (PEM)