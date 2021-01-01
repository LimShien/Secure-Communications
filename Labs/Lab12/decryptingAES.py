"""
ow modify  your coding for 256-bit AES ECB  encryption, so that  you can enter the cipher text, and an encryption key, and the  code  will decrypt to provide the result. You should use CMS forpadding. With this, determine the plaintext for the following (note, all the plain text values are countries around the World)

CMS Cipher (256-bit AES ECB)        Key             Plain text
b436bd84d16db330359edebf49725c62    “hello”         germany
4bb2eb68fccd6187ef8738c40de12a6b    “ankle”         spain

029c4dd71cdae632ec33e2be7674cc14    “changeme”      england
d8f11e13d25771e83898efdbad0e522c    “123456"        scotland
"""
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
val='4bb2eb68fccd6187ef8738c40de12a6b'
password="ankle"

if(len(sys.argv)>1):
    val = sys.argv[1]

if(len(sys.argv)>2):
    password = sys.argv[2]

ciphertext =val
plaintext = "Ireland"

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()


plaintext = decrypt(binascii.unhexlify(bytearray(val.encode())),key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='CMS')
print("  decrypt: ",plaintext)
