from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import binascii

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

p = int("0xde26ab651b92a129", 16)
g = int("0x2", 16)
A = int("0xc5f03d3a9a46f544", 16)
B = int("0x5fc0e0fcc19455b8", 16)
iv = "9bc4a935eaed052d1592363af76c9a12"
encrypted_flag = "3b390a9588dd4c08718e6056857b7e804f153f7d735e4f46a33a5fd4b48d991e"
print("p", p)
print("g", g)
print("A", A)
print("B", B)

for i in range(1000000,p):
    if(decrypt_flag(i, iv, encrypted_flag)[0:5] ==  bytes("crypto", "utf-8")):
        print(i)
        break

    
