"""We can write a Python program to implement this key exchange. Enter and run the
following program

Pick three different values for g and p, and make sure that the Diffie Hellman key exchange
works.
g =14 p= 1099
g= 21 p= 6007
g=  22 p= 7793
"""
import random
import base64
import hashlib
import sys
g=9
p=997

a=random.randint(5, 10)
b=random.randint(10,20)
A = (g**a) % p
B = (g**b) % p
print ('g: ',g,' (a shared value), n: ',p, ' (a prime number)')
print ('\nAlice calculates:')
print ('a (Alice random): ',a)
print ('Alice value (A): ',A,' (g^a) mod p')
print ('\nBob calculates:')
print ('b (Bob random): ',b)
print ('Bob value (B): ',B,' (g^b) mod p')
print ('\nAlice calculates:')
keyA=(B**a) % p
print ('Key: ',keyA,' (B^a) mod p')
#print ('Key: ',hashlib.sha256(str(keyA)).hexdigest())
print ('\nBob calculates:')
keyB=(A**b) % p
print ('Key: ',keyB,' (A^b) mod p')
#print ('Key: ',hashlib.sha256(str(keyB)).hexdigest())

