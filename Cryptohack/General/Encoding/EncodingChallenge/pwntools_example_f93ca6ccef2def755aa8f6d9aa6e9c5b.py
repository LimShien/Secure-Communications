from pwn import * # pip install pwntools
import json
import base64

from Crypto.Util.number import bytes_to_long, long_to_bytes



def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(s,t):
    if t == "base64":
        return d_base64(s)
    elif t =="rot13":
        return d_rot13(s)
    elif t=="hex":
        return d_hex(s)
    elif t =="bigint":
        return d_bigint(s)
    else:
        return d_utf8(s)
def d_rot13(s):  	
    abc= "abcdefghijklmnopqrstuvwxyz"
    result =""
    for x in s:
        if x == '_':
            position = x
            result += x
        else:
            if x.islower():
                position = abc.find(x)-13    
            else:
                position = abc.find(x.lower())-13

            if position <0:
                position += 26

            if  x.isupper():
                result += abc[position].upper()


            else:
                result += abc[position]

    return result

def d_base64(s):
    return str(base64.b64decode(s),"utf-8")
def d_hex(s):
    result =""
    for x in bytearray.fromhex(s):
        result+=chr(x)

    return result
def d_bigint(s):
    if(s[0] == '0' and s[1] == 'x'):
        z = int(s, 16)
        return str(long_to_bytes(z),encoding="utf-8")
    else:
        return str(long_to_bytes(s),encoding="utf-8")
    

def d_utf8(s):
    result=""
    for x in s:
        result += chr(x)
    return result

r = remote('socket.cryptohack.org', 13377, level = 'debug')
for i in range(101):
    received = json_recv()


    to_send = {
        "decoded": decode(received["encoded"],received["type"])
    }
    

    json_send(to_send)
    

