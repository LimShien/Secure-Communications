"""
While APR1 has a salted value, the SHA-1 hash does not have a salted value. It produces a
160-bit signature, thus can contain a larger set of hashed value than MD5, but because there is
no salt it can be cracked to rainbow tables, and also brute force. The format for the storage of
the hashed password on Linux systems is:
# htpasswd -nbs bill hello
bill:{SHA}qvTGHdzF6KLavt4PO0gs2a6pQ00=
We can also generate salted passwords with crypt, and can use the Python script of:
import passlib.hash;
salt="8sFt66rZ"
string="hello"
print "SHA1:"+passlib.hash.sha1_crypt.encrypt(string, salt=salt)
print "SHA256:"+passlib.hash.sha256_crypt.encrypt(string, salt=salt)
print "SHA512:"+passlib.hash.sha512_crypt.encrypt(string, salt=salt)
SHA-512 salts start with $6$ and are up to 16 chars long.
SHA-256 salts start with $5$ and are up to 16 chars long
Which produces:
SHA1:$sha1$480000$8sFt66rZ$klAZf7IPWRN1ACGNZIMxxuVaIKRj
SHA256:$5$rounds=535000$8sFt66rZ$.YYuHL27JtcOX8WpjwKf2VM876kLTGZHsHwCBbq9x
TD
SHA512:$6$rounds=656000$8sFt66rZ$aMTKQHl60VXFjiDAsyNFxn4gRezZOZarxHaK.Tcp



F.1 Create a Python script to create the SHA hash for the following:
Prove them against on-line SHA generator(or from the page given above).

changeme SHA 1 changeme$sha1$480000$8sFt66rZ$dNfLzeD4O48TgFqDKd0zBYc4SJ5a
        SHA256 changeme$5$rounds=535000$8sFt66rZ$yNCVBp7NMi3UNzMEIoGoGnQZ.HMGaUETwiQNCBi/cl5
        SHA512changeme$6$rounds=656000$8sFt66rZ$B/.Msj2UuS3qH.Qxsy.RL82oni6MV75LZ8olN6eCw6.LSHCCcJ4IGnzdX9Qv299whMbpz4rR9e7A9Ab0L3ZA0/


123456  SHA 1 123456$sha1$480000$8sFt66rZ$RndE8VtL.VnDBVLPgp7vKcVb0BaN
        SHA256 123456$5$rounds=535000$8sFt66rZ$rAkO4NCQq4l0DjDAJFh2f6s9Ew.Y7qCIM7okpuHJR30
        SHA512123456$6$rounds=656000$8sFt66rZ$cGaBfax5eeGRKwD.bFK0IFUvrk0jyyeWKIkIsmWX0H9xvJco6OwFPZ5QA4jh5mZnt1w9FlhO2pKlhkpPHICts0
        
password SHA 1 password$sha1$480000$8sFt66rZ$h0Q07GoRgcYjKiYsjpufby/P7cf0
        SHA256 password$5$rounds=535000$8sFt66rZ$63AbYmdfWxNIp9x75xK4zBgdQxvzMGtNzpyI6DKhvb7
        SHA512password$6$rounds=656000$8sFt66rZ$hiU32dGMdhmg9uxrHHBnVz1j5A35Ap193q.Naf9kUkP.e1klwhfPW3Lv/LIydTiS97Adp5zYGN.1RM8s6NcNy/


"""
import passlib.hash;

salt = "8sFt66rZ"
s1 = 'changeme'
s2 = '123456'
s3 = 'password'
print(s1)
print("SHA 1 " + s1 + passlib.hash.sha1_crypt.encrypt(s1, salt= salt))
print("SHA256 " + s1 + passlib.hash.sha256_crypt.encrypt(s1, salt= salt))
print("SHA512" + s1 + passlib.hash.sha512_crypt.encrypt(s1, salt= salt))

print(s2)
print("SHA 1 " + s2 + passlib.hash.sha1_crypt.encrypt(s2 ,salt= salt))
print("SHA256 " + s2 + passlib.hash.sha256_crypt.encrypt(s2, salt= salt))
print("SHA512" + s2+ passlib.hash.sha512_crypt.encrypt(s2, salt= salt))

print(s3)
print("SHA 1 " + s3 + passlib.hash.sha1_crypt.encrypt(s3, salt= salt))
print("SHA256 " + s3 + passlib.hash.sha256_crypt.encrypt(s3,salt= salt))
print("SHA512" + s3 + passlib.hash.sha512_crypt.encrypt(s3,salt= salt))