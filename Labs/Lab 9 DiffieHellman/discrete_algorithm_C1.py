"""
 C discrete Algorithm
        1   ElGamal and Diffie Hellman use discrete logarithms. This involves a generator value
            (g) and a prime number. A basic operation is gx (mod p). If p=11, and g=2, determine
            the results (the first two have already been completed):
            x        g**x % p
            1        2
            2        4
            3        8
            4        5
            5        10
            6        9
            7        7
            8        3
            9        6
            10       1
            11       2
            12       4

            What happens to the values once we go past 10?
            -the value go back to a loop / repeat pattern

            What happens to this sequence if we use g=3?
            -the group became five/ loop after the fifth 

"""


g = 3
p = 11

print("x", "\t", "g**x % p")
for i in range(1, 13):
    print(i , "\t" , pow(g,i,p))