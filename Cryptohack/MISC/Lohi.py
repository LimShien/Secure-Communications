import telnetlib
import json
import random
HOST = "socket.cryptohack.org"
PORT = 13383
tn = telnetlib.Telnet(HOST, PORT)
 

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


c =["Lower", "Higher"]

print(readline())

for i in range(1, 101):
    z = 0
    if i % 10 ==0:
        if z > 0:
            z = 0
        else: 
            z = 1
        
    x =c[z]
    request = {"choice": x}
    json_send(request)
    print(json_recv())



