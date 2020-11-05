#! /usr/bin/python3
from binascii import unhexlify,hexlify

c = 97938185189891786003246616098659465874822119719049
e = 65537
n = 196284284267878746604991616360941270430332504451383 # for p and q use https://www.alpertron.com.ar/ECM.HTM

p = 10252256693298561414756287
q = 19145471103565027335990409

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinverse(a, m): # modular inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

phi = (p-1) * (q-1)

d = modinverse(e,phi)

print("Private Key: "+str(d))

m = pow(c,d,n)

flag = unhexlify(hex(m)[2:])
print("Bitchy Flag: "+ str(flag.decode()))
