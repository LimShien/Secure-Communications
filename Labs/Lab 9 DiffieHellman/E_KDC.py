"""
Rather than using key exchange, we can setup a KDC, and where Bob and Alice can have longterm keys. These can be used to generate a session key for them to use. Enter the following
Python program, and prove its operation:


The program above uses a shared 128-bit session key (generated by MD5). Now change the
program so that you generate a 256-bit session key. What are the changes made:

keySession= hashlib.md5(str(rnd).encode()).hexdigest() - > keySession= hashlib.sha256(str(rnd).encode()).hexdigest()
"""
import hashlib
import sys
import binascii
import Padding
import random

from Crypto.Cipher import AES
from Crypto import Random

msg="test"

def encrypt(word,key, mode):
	plaintext=pad(word)
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	rtn = encobj.decrypt(ciphertext)
	return(rtn)

def pad(s):
	extra = len(s) % 16
	if extra > 0:
    		s = s + (' ' * (16 - extra))
	return s


rnd = random.randint(1,2**128)

keyA= hashlib.md5(str(rnd).encode()).digest()

rnd = random.randint(1,2**128)

keyB= hashlib.md5(str(rnd).encode()).digest()
 
print('Long-term Key Alice=',binascii.hexlify(keyA))
print('Long-term Key Bob=',binascii.hexlify(keyB))

rnd = random.randint(1,2**128)
keySession= hashlib.sha256(str(rnd).encode()).hexdigest()

ya = encrypt(keySession.encode(),keyA,AES.MODE_ECB)
yb = encrypt(keySession.encode(),keyB,AES.MODE_ECB)

print("Encrypted key sent to Alice:",binascii.hexlify(ya))
print("Encrypted key sent to Bob:",binascii.hexlify(yb))

decipherA = decrypt(ya,keyA,AES.MODE_ECB)
decipherB = decrypt(yb,keyB,AES.MODE_ECB)

print("Session key:",decipherA)
print("Session key:",decipherB)