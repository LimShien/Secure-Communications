"""
Now implement a Python program which will try various keys for a cipher text input, and show the decrypted text. The keys tried should be:["hello","ankle","changeme","123456"]
Run the program and try to crack:“1jDmCTD1IfbXbyyHgAyrdg==”

password :  norway

"""
from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
import base64
val='1jDmCTD1IfbXbyyHgAyrdg=='


if(len(sys.argv)>1):
    val = sys.argv[1]

if(len(sys.argv)>2):
    password = sys.argv[2]

ciphertext = base64.b64decode(val).hex()

key_arr = ["hello","ankle","changeme","123456"]

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))
try:

    for i in range(0,4):
        key = hashlib.sha256(key_arr[i].encode()).digest()
        plaintext = decrypt(binascii.unhexlify(bytearray(ciphertext.encode())),key,AES.MODE_ECB)
        if (len(Padding.removePadding(plaintext,mode='CMS')) >=1):
            plaintext = Padding.removePadding(plaintext,mode='CMS') 
            break

    
    print("  decrypt: ",plaintext)

except:
    print("erroe")

