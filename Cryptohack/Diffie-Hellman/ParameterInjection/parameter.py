import binascii 

d = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0x321fe0c7ce2e5b095c0622e6049771c2c42b430af989d18e50c6605bc7342cd7f97a02a5a8baf9e1cdaf86ad9e1f38a26f9549df321d11232df8675f570fa77182362f6dd2305a50a21715161b383c9624c300d2125d153d7fc4a5f112aa52846ad9cccdb6b7f9a0bdef1adcc86cc7d584b3731aba634ead65c4b3db12c87cd54e23020059032679b0d9e40288add0ec581134b1f60d6badb7edd88394d0706cc3d4fc33e4248b50d1ada5650eb35617f8932eff5e4233c9e6d5adba8ac54511"}

#using the fact that a^n mod a = 0
p = int(d.get("p"), 16)
g = int(d.get("g"), 16)
d["A"] = p
#d["B"] = p
print(pow(g, 4, p ))


