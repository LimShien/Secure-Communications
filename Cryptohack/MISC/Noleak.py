"""
Each time you connect, I generate a new one time pad. I also check for leaks, so there's no chance you can learn anything about my secrets!

Connect at nc socket.cryptohack.org 13370

"""
import telnetlib
import json

##code from cryptohack general section 
HOST = "socket.cryptohack.org"
PORT = 13370
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


request = {"msg": "request"}
json_send(request)
ct1 = json_recv()

request = {"msg": "request"}
json_send(request)
ct2 = json_recv()
print(ct1, ct2)
print("lTQPTuPpymAdhx0csPOMbM6ojDg="^"y9+a+HOqF7fylcvoFU9GoTPq45g=")