""""
Here is my super-strong RSA implementation, because it's 1600 bits strong it should be unbreakable... at least I think so!


"""
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373
##factorize in factorDB
phi = int((752708788837165590355094155871-1)*(986369682585281993933185289261-1))
## 1 = d*e mod phi 
d = inverse(e, phi)


# m = c^d mod n

print(long_to_bytes(pow(ct, d, n)))