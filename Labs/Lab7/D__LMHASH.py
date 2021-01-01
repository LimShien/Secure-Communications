"""
The LM Hash is used in Microsoft Windows. For example, for LM Hash:
hashme gives: FA-91-C4-FD-28-A2-D2-57-AA-D3-B4-35-B5-14-04-EE
network gives: D7-5A-34-5D-5D-20-7A-00-AA-D3-B4-35-B5-14-04-EE
napier gives: 12-B9-C5-4F-6F-E0-EC-80-AA-D3-B4-35-B5-14-04-EE
Notice that the right-most element of the hash are always the same, if the password is less
than eight characters. With more than eight characters we get:
networksims gives: D7-5A-34-5D-5D-20-7A-00-38-32-A0-DB-BA-51-68-07
napier123 gives: 67-82-2A-34-ED-C7-48-92-B7-5E-0C-8D-76-95-4A-50
For “hello” we get:
LM: FD-A9-5F-BE-CA-28-8D-44-AA-D3-B4-35-B5-14-04-EE
NTLM: 06-6D-DF-D4-EF-0E-9C-D7-C2-56-FE-77-19-1E-F4-3C
We can check these with a Python script:


        Create a Python script to determine the LM
        hash and NTLM hash of the following
        words:
        Napier
        LM Hash:12b9c54f6fe0ec80aad3b435b51404ee
        NT Hash:3ca6cef4b84985b6e3cd7b24843ea7d1
        Foxtrot
        LM Hash:82121098b60f69f5aad3b435b51404ee
        NT Hash:828f0524d3fffd8632ee97253183fef3
        """

import passlib.hash;
s1 = "Napier"
s2 = "Foxtrot"
print ("LM Hash:"+passlib.hash.lmhash.encrypt(s1))
print ("NT Hash:"+passlib.hash.nthash.encrypt(s1))
print ("LM Hash:"+passlib.hash.lmhash.encrypt(s2))
print ("NT Hash:"+passlib.hash.nthash.encrypt(s2))
