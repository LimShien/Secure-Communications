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
val='yebd'
password='hello'

if(len(sys.argv)>1):
    val = sys.argv[1]

if(len(sys.argv)>2):
    password = sys.argv[2]

plaintext= val

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()[:8]

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,DES.MODE_ECB)
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))
print(ciphertext)

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='CMS')
print("  decrypt: ",plaintext)

plaintext=val


plaintext = decrypt(ciphertext,key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='ZeroLen')
print("  decrypt: ",plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='Space')

print("After padding (Space): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,DES.MODE_ECB)
print("Cipher (Space): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='Space')
print("  decrypt: ",plaintext)


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='Random')

print("After padding (Random): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,DES.MODE_ECB)
print("Cipher (Random): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='Random')
print("  decrypt: ",plaintext)