import base64
import asn1
from Crypto.PublicKey import RSA

with open("/home/kali/College/Secure-Communications/Cryptohack/General/pk.pem") as f:
    key = RSA.importKey(f.read())

print(key.d)