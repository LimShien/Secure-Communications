"""
ow modify  your coding for 256-bit AES ECB  encryption, so that  you can enter the cipher text, and an encryption key, and the  code  will decrypt to provide the result. You should use CMS forpadding. With this, determine the plaintext for the following (note, all the plain text values are countries around the World)

CMS Cipher (256-bit AES ECB)        Key         Plain text

/vA6BD+ZXu8j6KrTHi1Y+w==            “hello”     italy
nitTRpxMhGlaRkuyXWYxtA==            “ankle”     sweden
irwjGCAu+mmdNeu6Hq6ciw==            “changeme”  belgium
5I71KpfT6RdM/xhUJ5IKCQ==            “123456”    mexico
"""
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
import base64
val='/vA6BD+ZXu8j6KrTHi1Y+w=='
password="hello1"

if(len(sys.argv)>1):
    val = sys.argv[1]

if(len(sys.argv)>2):
    password = sys.argv[2]

ciphertext = base64.b64decode(val).hex()


def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()


plaintext = decrypt(binascii.unhexlify(bytearray(ciphertext.encode())),key,AES.MODE_ECB)

plaintext = Padding.removePadding(plaintext,mode='CMS')
print("  decrypt: ",plaintext)
