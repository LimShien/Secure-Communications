"""
Now determine the cipher text for the following (the first example has already been completed):
Message         Key          CMS Cipher
“hello”         “hello123”      db8d4d4ddaea314f
“inkwell”      “orange”         1086a73ab5273254
“security”      “qwerty”        d19c86b3fc7e924f148652c183caa922
“Africa”        “changeme       d19c86b3fc7e924f148652c183caa922
"""
from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding
val='77533df9d91c2b3f'
password="changeme"

if(len(sys.argv)>1):
    val = sys.argv[1]

if(len(sys.argv)>2):
    password = sys.argv[2]

ciphertext =val


def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))
key = hashlib.sha256(password.encode()).digest()[:8]


plaintext = decrypt(binascii.unhexlify(val.encode()),key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='CMS')
print("  decrypt: ",plaintext)
