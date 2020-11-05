# Oligar's Tricky RSA

We have access to the following parameters: 

* **C** - ciphertext
* ***e*** - public exponent
* ***n*** - modulus

```
c = 97938185189891786003246616098659465874822119719049
e = 65537
n = 196284284267878746604991616360941270430332504451383
```

Obviously this challenge is about the **RSA**. In order to get the plaintext message, we need

> M = c^*d* mod n  --> *d* is the private key

We have all the info, except *d*. 

> *d* = *e* ^-1 mod *λ(n)*, phi or totient *λ(n)* =(p-1) * (q-1)

we need to find *p* and *q*. These are prime numbers which make up ***n***.

This is the tricky part of the challenge because 
> ***n*** = *p* * *q*

Factorization is a hard problem to solve. In this case to speed things a llitle bit I used the tool [Fatorization Calculator](https://www.alpertron.com.ar/ECM.HTM).

The output shows *p* and *q*.

Now we can calculate the totient *λ(n)* and have *d* and decrypt the flag.

[solve.py](https://github.com/s4nkx0k/CTFs/blob/main/NACTF%202020/Oligar's%20Tricky%20RSA/solve.py)
