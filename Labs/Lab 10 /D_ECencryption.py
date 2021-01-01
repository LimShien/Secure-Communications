""""D.1In the following Bob and Alice create elliptic curve key pairs. Bob can encrypt a message for Alice with her public key, and she can decrypt with her private key. Copy and paste the program from here"""
import OpenSSL
import pyelliptic
secretkey="password"
test="Test123"
alice = pyelliptic.ECC() 
bob = pyelliptic.ECC()
print ("++++Keys++++")
print ("Bob's private key: "+bob.get_privkey().encode('hex'))
print ("Bob's public key: "+bob.get_pubkey().encode('hex'))
print()
print ("Alice's private key: "+alice.get_privkey().encode('hex'))
print ("Alice's public key: "+alice.get_pubkey().encode('hex'))
ciphertext = alice.encrypt(test, bob.get_pubkey())
print ("\n++++Encryption++++")
print ("Cipher: "+ciphertext.encode('hex'))
print ("Decrypt: "+bob.decrypt(ciphertext))
signature = bob.sign("Alice")
print ()
print ("Bob verified: "+ str(pyelliptic.ECC(pubkey=bob.get_pubkey()).verify(signature, "Alice")))

