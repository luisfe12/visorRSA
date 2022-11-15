from Crypto.PublicKey import RSA

f = open('luisfe.pem','r')

key = f.read()

print(len(key))
private_key_pem = key

private_key = RSA.importKey(private_key_pem)
print("private key components:")
print("modulus:", private_key.n)
print("publicExponent:", private_key.e)
print("privateExponent:", private_key.d)
print("prime1:", private_key.p)
print("prime2:", private_key.q)
print("exponent1:", private_key.d)
print("decryption key:", private_key.d, "\n")
