from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val='Africa'
password='changeme'
if(len(sys.argv)>1):

	val = sys.argv[1]

if (len(sys.argv)>2):

	password = sys.argv[2]


plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode('utf-8')).digest()


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
print ("After padding (CMS): ")
print(binascii.hexlify(bytearray(plaintext, 'utf-8')))

ciphertext = encrypt(plaintext.encode('utf-8'),key,AES.MODE_ECB)
print ("Cipher (ECB): ")
print(binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(plaintext.encode('utf-8'),key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='CMS')
print ("  decrypt: ")
print(plaintext)


plaintext=val


plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print ("\nAfter padding (Bit): ")
print(binascii.hexlify(bytearray(plaintext, 'utf-8')))

ciphertext = encrypt(plaintext.encode('utf-8'),key,AES.MODE_ECB)
print ("Cipher (ECB): ")
print(binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print ("  decrypt: ")
print(plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print ("\nAfter padding (Null): ")
print(binascii.hexlify(bytearray(plaintext, 'utf-8')))

ciphertext = encrypt(plaintext.encode('utf-8'),key,AES.MODE_ECB)
print ("Cipher (ECB): ")
print(binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print ("  decrypt: ")
print(plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext.encode('utf-8'),blocksize=Padding.AES_blocksize,mode='Random')
print ("\nAfter padding (Random): ")
print(binascii.hexlify(bytearray(plaintext)))

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print ("Cipher (ECB): ")
print(+binascii.hexlify(bytearray(ciphertext)))

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext,mode='Random')
print ("  decrypt: ")
print(plaintext)
