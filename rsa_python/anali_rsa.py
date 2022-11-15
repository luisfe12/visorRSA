from Crypto.PublicKey import RSA


def saber_pu_pr(llave_string):
    pass

def Analizar_PrK(direccion):
    f = open(direccion,'r')

    key = f.read()
    
    #print(type(key))

    print(len(key))
    private_key_pem = key
    private_key = RSA.importKey(private_key_pem)
    texto_rsakM = "private key components: \n"
    #print("private key components:")
    #print("modulus:", private_key.n)
    texto_rsakM  = texto_rsakM + "modulus:\t "
    texto_rsakM = texto_rsakM + str(private_key.n) + "\n \n"
    #print(texto_rsakM)
    #print("publicExponent:", private_key.e)
    texto_rsakM  = texto_rsakM + "publicExponent: \t"
    texto_rsakM = texto_rsakM + str(private_key.e) + "\n \n"
    #print("privateExponent:", private_key.d)
    texto_rsakM  = texto_rsakM + "privateExponent: \t"
    texto_rsakM = texto_rsakM + str(private_key.d) + "\n \n"
    #print("prime1:", private_key.p)
    texto_rsakM  = texto_rsakM + "prime1: \t"
    texto_rsakM = texto_rsakM + str(private_key.p) + "\n \n"
    #print("prime2:", private_key.q)
    texto_rsakM  = texto_rsakM + "prime2: \t"
    texto_rsakM = texto_rsakM + str(private_key.q) + "\n \n"
    #print("exponent1:", private_key.d)
    texto_rsakM  = texto_rsakM + "exponent1: \t"
    texto_rsakM = texto_rsakM + str(private_key.d) + "\n \n"
    #print("decryption key:", private_key.d, "\n")
    texto_rsakM  = texto_rsakM + "decryption key: \t"
    texto_rsakM = texto_rsakM + str(private_key.d) + "\n \n"

    print(texto_rsakM)
    return texto_rsakM

def Analizar_PuK(direccion):
    f = open(direccion,'r')

    key = f.read()
    public_key_pem = key
    public_key = RSA.importKey(public_key_pem)

    #ingresamo valores
    txt_pu_Con = "public key components: \n"
    #print("public key components:")

    #print("modulus:", public_key.n)
    txt_pu_Con =  txt_pu_Con + "modulus: \t"
    txt_pu_Con =  txt_pu_Con + str(public_key.n) + "\n \n"
    #print("encryption key:", public_key.e)
    txt_pu_Con =  txt_pu_Con + "encryption key: \t"
    txt_pu_Con =  txt_pu_Con + str(public_key.e) + "\n \n"

    print(txt_pu_Con)
    return txt_pu_Con

def analizar(direccion):
    f = open(direccion,'r')

    key = f.read()

    if "PRIVATE" in key:
        valpr = Analizar_PrK(direccion)
        return valpr
    elif "PUBLIC" in key:
        valpu = Analizar_PuK(direccion)
        return valpu




#Estes
private_key_pem='''-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA3fJtY+4/TSuZ07iVqGq6Xa9QMFeor5JZwy7IfyyNOHeVFRSS
dYBo8WDTHTe4flJsRspHa1pI72v1yoJQJ3M7DFAtAxiHzqhAyYZ4wjdxTN8YBVl5
qqbRr7OKTvM8s3Z+2O7aG+ayIyeFKf0DX2ajFkOD3/ql6ne1pQUPCSjLNRSRYdCe
e03eKVw6ORSBUe262gEDf/UWHisg3o2JaVLcmR3ps4ESRcdx0AZ9hYWONGmHn7Fs
NiSp1ry8SVTOnfdcuvjVVfKLVaOui7nntU5OxQijz+/kk4vy58qDedyHxB24wMt6
S+7a5P++ZO20K4/mBIFmdyGIuvOYJY0Gs7X/EQIDAQABAoIBAQDSqNNjUjMLECNF
baG+5O5XFZtLByi43HQOak0rSCISQo5iH9CTbnotAPXgeY7Hd3wGBOCc6GjpttLo
j598kkatfTv8AECGyfQUU2ozDWSgze+CxFZSv1uvJP5VyVEIFaR4St0CNolGDLC8
FcYpusV40ERPRxxL26uxIYgP7YRSr5nReJrZU3xVaBIPxRVmPnJD/7MhaiwkZI53
Trwgp7Za3cXMLxetSXV4mRcyejKUYac+OWrf9/gvvFWegHRHJPz5AfS6jo8qPPy0
HO+yW3w9psSSYv7n+P5hHk6uqfEnPjp80ke+MxPtRTT2+OpjypToZiL4nNZmppA2
p5vQf0NxAoGBAPvLQ2YGZsP4uvbLrRMbFzaVlfiXnwGU4gJ4R2nf6OnKWhWqTI6W
TxuUS5VJetgSgSU721LjGvyBjwJWa7mMmfHnmrZqW7AKNKVlpUqx7nsUy9YHfV7o
zZTXBZxgMEiCWxHYl36DdGbEclQDitjFH+ur8TaVIo7xewZ/cgOudqK/AoGBAOGn
h8lpqoP0U/49BpznMhN1trBct4uLs+EYgK5Dtu2+RQCoApHCQ9QLLFjvVv3plyVm
Hy9+MHovxl9hQ1C6RqIpncWlGiI52gr4tGCiM+VMTQ8h2qOESfSJHqd4hivcHDsZ
/1HDETQa6vF3b/zyXDAQxstBhotHqhdZEHMTn2IvAoGAEI0n/QjmsHMlNxvkYKEj
QX9LwG+XEC+NO8RUTW1ejh+zFEGBjs3qnVF+Nm4CGTn+K0hn/mbXW0nY8Lplkmjf
pbsnvF35cPT6yPSJjQNtPcH8NDGB2D9NZD9OKx1Xjyyid+XY74QMnsTDDyq8cctj
ccZ3sLLU9riA8chm4j8RpVkCgYEA0Xi4N0Nss6OKmPbDfcGsnZ3nYh4fkF22NJ2P
TrWzSU0YNvy/rdkdJ+jbWQ+MvJYr5d6/0lGc5MAWsRHT8EuLKBvjxsZ11RHJE+g9
YXsRG6lR21s84A/8qxDisOnT+0EPv9lpRtgCz1CxikeqYLAG3eOk9qe0IvT6s0PN
XlX33acCgYEAq97EBQqEUusOOnut5Or89+j1e0A7NywSfiWYl0As8hwuxApAYtyV
sHgiPtRCjfD8UcWyD9cbL2Vk/6ZI85u0n7J+OO9ep6pyrMDlCMrx6gEuskyTalsp
ggB5+scSGkfSpCI/Hm2UvQUYf+QzYWpgy0yTmCrFoHibkTKHZQAzsVE=
-----END RSA PRIVATE KEY-----
'''

public_key_pem='''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3fJtY+4/TSuZ07iVqGq6
Xa9QMFeor5JZwy7IfyyNOHeVFRSSdYBo8WDTHTe4flJsRspHa1pI72v1yoJQJ3M7
DFAtAxiHzqhAyYZ4wjdxTN8YBVl5qqbRr7OKTvM8s3Z+2O7aG+ayIyeFKf0DX2aj
FkOD3/ql6ne1pQUPCSjLNRSRYdCee03eKVw6ORSBUe262gEDf/UWHisg3o2JaVLc
mR3ps4ESRcdx0AZ9hYWONGmHn7FsNiSp1ry8SVTOnfdcuvjVVfKLVaOui7nntU5O
xQijz+/kk4vy58qDedyHxB24wMt6S+7a5P++ZO20K4/mBIFmdyGIuvOYJY0Gs7X/
EQIDAQAB
-----END PUBLIC KEY-----
'''

#Analizar_PrK('/home/luisfe/Documents/pythonPr/rsa_python/luisfe.pem')

# private_key = RSA.importKey(private_key_pem)
# print("private key components:")
# print("modulus:", private_key.n)
# print("publicExponent:", private_key.e)
# print("privateExponent:", private_key.d)
# print("prime1:", private_key.p)
# print("prime2:", private_key.q)
# print("exponent1:", private_key.d)
# print("decryption key:", private_key.d, "\n")

# public_key = RSA.importKey(public_key_pem)
# print("public key components:")
# print("modulus:", public_key.n)
# print("encryption key:", public_key.e)