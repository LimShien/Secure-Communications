"""
Alice and Bob are using legacy codebases and need to negotiate parameters they both support. You've man-in-the-middled this negotiation step, and can passively observe thereafter. How are you going to ruin their day this time?
"""
import math
from math import ceil, sqrt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import binascii
import telnetlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
import sagemath

"""
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

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

HOST = "socket.cryptohack.org"
PORT = 13373

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline()[24:])
print(readline())
print(readline())
print(readline())

print(readline())
print(readline())


request = {
    "supported": "DH64"
}
json_send(request)

response = json_recv()

print(response) """


# This code is contributed by mits


p = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
g = "0x02"
A = "0x16dfba2e2a4c2992854d24a0eb3bf11a0f4bb46a229db7540e5ce7b62652780338da20d1cae883895d2d1b1b8fc6fffdce336ae6dfe90ec4856ec4d861f0e41329c85430dcccb5218a1afafc571d4f43479f56417f21638b38d33971c49c18c30f028f2675e4ec83d87ced581600606198b1d8ee2f4f999fe701229b130dc5abb37d6d716af2b656084a350e395c50786e951467860f5cfb7fa45722fad329d39f88fcb0fa5bef81c5dd0e7930b84cc7f064ab4de58858fa4cb800d5fa9b68b2"
B = "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"
iv = "eb5716f8d0bc37fc6bc27c6428ca75d9"
encrypted = "91a4f395ced6f18a7f83f85a11e7774054076c473e5e752758efa71aa8068983"
"""
g^a mod p = A
g^b mod p = B

A^b mod p = B^a mod p
"""

p = int(p, 16)
g = int(g, 16)
A = int(A, 16)
B = int(B, 16)
print(p, g, A, B)

