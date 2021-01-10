"""
I won't have have to worry about running out of entropy, I'm going to have my OTP generated forever with this new script!

Connect at nc socket.cryptohack.org 13372

"""
import telnetlib
import json

##code from cryptohack general section 
HOST = "socket.cryptohack.org"
PORT = 13372
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


request = {"option": "get_flag"}
json_send(request)

flag = json_recv()
print(str(flag)[20:76])  ##parse th output ?
request = {"option": "encrypt_data", "input_data": str(flag)[20:76]} ##encrypt the encrypted flag to get the original  , using XOR theory, 
json_send(request)
print(json_recv()) ##output the same hex string for every instance, isuppose the hex string is the flag

print(bytes.fromhex("63727970746f7b7430305f663473745f7430305f667572693075357d"))