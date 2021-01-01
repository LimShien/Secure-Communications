# This is the program we believe was used to encode the intercepted message.
# some of the retrieved program was damaged (show as &&&&)
# Can you use this to figure out how it was encoded and decode it? 
# Good Luck

import string
import random
from base64 import b64encode, b64decode

secret = 'hey' # We don't know the original message or length

secret_encoding = ['step1', 'step2', 'step3']

def step1(s):
	_step1 = string.maketrans("zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA","mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON")
	return string.translate(s, _step1)

def step2(s): return b64encode(s)

def step3(plaintext, shift=4):
    loweralpha = string.ascii_lowercase
    shifted_string = loweralpha[shift:] + loweralpha[:shift]
    converted = string.maketrans(loweralpha, shifted_string)
    return plaintext.translate(converted)

def make_secret(plain, count):
	print "pt =", plain
	a = '2{}'.format(b64encode(plain))  #the code adds a '2' at the beginning 
	print "ptb64 = " , a, "c = ", count
	for count in xrange(count):
		r = random.choice(secret_encoding)
		print r
		si = secret_encoding.index(r) + 1
		_a = globals()[r](a)
		print "_a", _a
		a = '{}{}'.format(si, _a)
		print "a", a
	return a

if __name__ == '__main__':
	print make_secret("test", count=5) 

	
	


