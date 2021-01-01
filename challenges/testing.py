from base64 import b64encode, b64decode



import string
import random
from base64 import b64encode, b64decode
import sys

secret = sys.argv[0]
print(secret)

##if step one, reverse the map
##if step 2 , decode instead of encode
##if step 3, minus shift 4
#write a function to determine the first number 

def step1(s):
	_step1 = string.maketrans("mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON", "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA")
	return string.translate(s, _step1)
def step2(s): return b64decode(s)

def step3(plaintext, shift=-4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def decode(ct):
#check if the first char is digit
#[1:] to remove the first char at index 0 
#[0) to return the char at index 0    
    while(True):
        if(ct[0].isdigit()):
            if(int(ct[0]) == 1):
                ct = step1(ct[1:])
            elif(int(ct[0]) == 2):
                ct = step2(ct[1:])
            elif(int(ct[0]) == 3):
                ct = step3(ct[1:])
        else:
            break
    return ct


print(decode(secret))


