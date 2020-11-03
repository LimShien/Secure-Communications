"""I've hidden my data using XOR with a single byte. Don't forget to decode from hex first.

73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"""
from pwn import xor
from binascii import unhexlify

key=unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for i in range(256):

    print(xor(key,i,cut="max"))