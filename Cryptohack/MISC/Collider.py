"""
Check out my document system about particle physics, where every document is uniquely referenced by hash.

Connect at nc socket.cryptohack.org 13389

13389.py
"""

import telnetlib
import json

##code from cryptohack general section 
HOST = "socket.cryptohack.org"
PORT = 13389
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

##reading the source code, it says that if MD5 of two different string collide, the flag is ..,.
##the collision from https://www.mscs.dal.ca/~selinger/md5collision/

request = {"document": "d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70"}
json_send(request)
print(json_recv())
request = {"document": "d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70 "}
json_send(request)
print(json_recv())