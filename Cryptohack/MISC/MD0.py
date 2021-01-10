"""
I've invented a nice simple version of HMAC authentication, hopefully it isn't vulnerable to the same problems as Merkle–Damgård construction hash functions...

Connect at nc socket.cryptohack.org 13388

"""
#
import telnetlib
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def bxor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def hash(data):
    data = pad(data, 16)
    out = b"\x00" * 16
    for i in range(0, len(data), 16):
        blk = data[i:i+16]
        out = bxor(AES.new(blk, AES.MODE_ECB).encrypt(out), out)
    return out

##code from cryptohack general section 
HOST = "socket.cryptohack.org"
PORT = 13388
tn = telnetlib.Telnet(HOST, PORT)
 

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


print(readline())

request = {"option": "sign", "message": ""}
json_send(request)
print(json_recv()["signature"])
request = {"option": "get_flag", "signature" : json_recv()["signature"]}
json_send(request)
print(json_recv())
