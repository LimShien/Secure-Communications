"""Bob and Alice agree on a g value of 5, and a prime number of 97. They then use the
Diffie-Hellman key exchange method. Alice passes a value of 32, and Bob passes a value
of 41. Can you determine the secret value that Bob and Alice have generated, and the
resultant key value? Outline the code here:

What happens if we use a g value of 2? Why is there a problem?
- error occurred in the program, 2 is not primitive rood mod to 97

Can you now write a generate DH key cracker for any value of g, p, A (passed by Alice), and
B (passed by Bob) Outline code and run to evaluate the perform of our code with different
ranges of the prime number (p):

"""
#g ** x mod p
g = 5
p = 4013

A = 300

B  = 41

for i in range(p):
    if(pow(g, i, p)== A):
        print("Alice secret: " , i)
        a = i
        break

for i in range(p):
    if(pow(g, i, p) == B):
        print("Bob secret: " , i)
        b = i
        break

print("Alice shared ", pow(B, a, p))

print("Bob shared ", pow(A, b, p))

#print(pow(g,b,p))