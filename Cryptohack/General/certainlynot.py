from Crypto.PublicKey import RSA
import asn1
from asn1crypto.x509 import Certificate
from cryptography import x509
from cryptography.hazmat.backends import default_backend


der = open("/home/kali/College/Secure-Communications/Cryptohack/General/2048b-rsa-example-cert.der", "rb").read()
cert = x509.load_der_x509_certificate(der, default_backend())
