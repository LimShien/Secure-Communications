""" I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!

0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104 """

from binascii import unhexlify
from pwn import xor

flag = unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
hint= bytes("crypto{}", "utf-8")
#print(xor(flag,hint,cut="max"))
for i in range(8):
    print(chr(flag[i]^hint[i]), end="")

print()
c=0
for i in flag:
    c+=1
    print(i, end=" ")
print("c =", c)

sk=bytes("myXORkey","utf-8")
print(xor(sk, flag,cut="max"))