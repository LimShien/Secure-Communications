"""
Now determine the cipher text for the following (the first example has already been completed):
Message         Key          CMS Cipher
“hello”         “hello123”      0a7ec77951291795bac6690c9e7f4c0d
“inkwell”      “orange”     
“security”      “qwerty”
“Africa”        “changeme
"""
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
val='hello'
password='hello'

if(len(sys.argv)>1):
    val = sys.argv[1]

if(len(sys.argv)>2):
    password = sys.argv[2]

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')

print("After padding (CMS): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print(ciphertext)
print("Cipher (ECB): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='CMS')
print("  decrypt: ",plaintext)

plaintext=val


plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='ZeroLen')
print("  decrypt: ",plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')

print("After padding (Space): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print("Cipher (Space): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='Space')
print("  decrypt: ",plaintext)


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Random')

print("After padding (Random): ",binascii.hexlify(bytearray(plaintext.encode())))

ciphertext = encrypt(plaintext.encode(),key,AES.MODE_ECB)
print("Cipher (Random): ",binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='Random')
print("  decrypt: ",plaintext)