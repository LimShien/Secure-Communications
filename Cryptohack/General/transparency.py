"""
Attached is an RSA public key in PEM format. Find the subdomain of cryptohack.org which uses these parameters in its TLS certificate, and visit that subdomain to obtain the flag.

"""

##https://pem.readthedocs.io/en/stable/core.html
import pem

with open("/home/kali/College/Secure-Communications/Cryptohack/General/transparency.pem", "rb") as f:
   certs = pem.parse(f.read())

print(certs)

with open("/home/kali/College/Secure-Communications/Cryptohack/General/cryptohack-org-1.pem", "rb") as f:
   certs = pem.parse(f.read())

print(certs)

with open("/home/kali/College/Secure-Communications/Cryptohack/General/cryptohack-org.pem", "rb") as f:
   certs = pem.parse(f.read())

print(certs)