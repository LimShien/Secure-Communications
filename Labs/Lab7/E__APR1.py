"""
The Apache-defined APR1 format addresses the problems of brute forcing an MD5 hash, and
basically iterates over the hash value 1,000 times. This considerably slows an intruder as they
try to crack the hashed value. The resulting hashed string contains “$apr1$” to identify it and
uses a 32-bit salt value. We can use both htpassword and Openssl to compute the hashed
string (where “bill” is the user and “hello” is the password):
# htpasswd -nbm bill hello
bill:$apr1$PkWj6gM4$XGWpADBVPyypjL/cL0XMc1
# openssl passwd -apr1 -salt PkWj6gM4 hello
$apr1$PkWj6gM4$XGWpADBVPyypjL/cL0XMc1
We can also create a simple Python program with the passlib library, and add the same salt as
the example above:
import passlib.hash;
salt="PkWj6gM4"
string="hello"
print "APR1:"+passlib.hash.apr_md5_crypt.encrypt(string, salt=salt)
We can created a simple Python program with the passlib library, and add the same salt as the
example above:
APR1:$apr1$PkWj6gM4$XGWpADBVPyypjL/cL0XMc1



    Create a Python script to create the APR1  hash for the following:
    Prove them against on-line APR1 generator
    (or from the page given above).


    APR1: changeme : $apr1$pkwj6gM4$an7iPvVcnNc3ocPcxh/DG1
    APR1: 123456 : $apr1$pkwj6gM4$RIt.SLUiDLHgfO8xI3JkB.
    APR1: password : $apr1$pkwj6gM4$L2t.3JppruqF3ECNT6x471

    """

import passlib.hash


salt = "pkwj6gM4"
s1 = "changeme"
s2 = "123456"
s3 = "password"
print("APR1: " + s1+ " : " + passlib.hash.apr_md5_crypt.encrypt(s1, salt=salt))
print("APR1: " + s2+ " : " + passlib.hash.apr_md5_crypt.encrypt(s2, salt=salt))
print("APR1: " + s3+ " : " + passlib.hash.apr_md5_crypt.encrypt(s3, salt=salt))