"""
MD5 and SHA-1 produce a hash signature, but this can be attacked by rainbow tables. Bcrypt
(Blowfish Crypt) is a more powerful hash generator for passwords and uses salt to create a nonrecurrent hash. It was designed by Niels Provos and David Mazières, and is based on the
Blowfish cipher. It is used as the default password hashing method for BSD and other systems.
9
Overall it uses a 128-bit salt value, which requires 22 Base-64 characters. It can use a number
of iterations, which will slow down any brute-force cracking of the hashed value. For example,
“Hello” with a salt value of “$2a$06$NkYh0RCM8pNWPaYvRLgN9.” gives:
$2a$06$NkYh0RCM8pNWPaYvRLgN9.LbJw4gcnWCOQYIom0P08UEZRQQjbfpy
As illustrated in Figure 1, the first part is "$2a$" (or "$2b$"), and then followed by the number
of rounds used. In this case is it 6 rounds which is 2^6 iterations (where each additional round
doubles the hash time). The 128-bit (22 character) salt values comes after this, and then finally
there is a 184-bit hash code (which is 31 characters).
The slowness of bcrypt is highlighted with an AWS EC2 server benchmark using hashcat:
• Hash type: MD5 Speed/sec: 380.02M words
• Hash type: SHA1 Speed/sec: 218.86M words
• Hash type: SHA256 Speed/sec: 110.37M words
• Hash type: bcrypt, Blowfish(OpenBSD) Speed/sec: 25.86k words
• Hash type: NTLM. Speed/sec: 370.22M words
You can see that Bcrypt is almost 15,000 times slower than MD5 (380,000,000 words/sec
down to only 25,860 words/sec). With John The Ripper:
• md5crypt [MD5 32/64 X2] 318237 c/s real, 8881 c/s virtual
• bcrypt ("$2a$05", 32 iterations) 25488 c/s real, 708 c/s virtual
• LM [DES 128/128 SSE2-16] 88090K c/s real, 2462K c/s virtual
where you can see that BCrypt over 3,000 times slower than LM hashes. So, although the main
hashing methods are fast and efficient, this speed has a down side, in that they can be cracked
easier. With Bcrypt the speed of cracking is considerably slowed down, with each iteration
doubling the amount of time it takes to crack the hash with brute force. If we add one onto the
number of rounds, we double the time taken for the hashing process. So, to go from 6 to 16
increase by over 1,000 (210) and from 6 to 26 increases by over 1 million (220).


H.1 Create the hash for the word “hello” for the different methods (you only have to give the
first six hex characters for the hash):
Also note the number hex characters that the hashed value uses:

        MD5:5d4140
        SHA1:aaf4c6
        SHA256:2cf24d
        SHA512:9b71d2
        DES:ZDVX7N
        MD5:$1$ZDz
        Sun MD5:$md5,r
        SHA1:$sha1$
        SHA256:$5$rou
        SHA512:$6$rou
        Bcrypt:$2b$12
"""

import hashlib
import passlib.hash

salt = "ZDzPE45C"
string = "hello".encode("utf-8")
salt2="1111111111111111111111"
print ("MD5:"+hashlib.md5(string).hexdigest()[:6])
print ("SHA1:"+hashlib.sha1(string).hexdigest()[:6])
print ("SHA256:"+hashlib.sha256(string).hexdigest()[:6])
print ("SHA512:"+hashlib.sha512(string).hexdigest()[:6])
print ("DES:"+passlib.hash.des_crypt.encrypt(string, salt=salt[:2])[:6])
print ("MD5:"+passlib.hash.md5_crypt.encrypt(string, salt=salt)[:6])
print ("Sun MD5:"+passlib.hash.sun_md5_crypt.encrypt(string, salt=salt)[:6])
print ("SHA1:"+passlib.hash.sha1_crypt.encrypt(string, salt=salt)[:6])
print ("SHA256:"+passlib.hash.sha256_crypt.encrypt(string, salt=salt)[:6])
print ("SHA512:"+passlib.hash.sha512_crypt.encrypt(string, salt=salt) [:6])
print ("Bcrypt:"+passlib.hash.bcrypt.encrypt(string, salt=salt2[:22]) [:6])