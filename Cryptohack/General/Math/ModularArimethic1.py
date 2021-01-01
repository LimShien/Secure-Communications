"""
ormally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if a ≡ b mod m.

Another way of saying this, is that when we divide the integer a by m, the remainder is b. This tells you that if m divides a (this can be written as m | a) then a ≡ 0 mod m.
"""


a = 0

c1 = 8146798528947%17
while(True):
    a += 1

    if(a%17== c1):
        break
print(a)