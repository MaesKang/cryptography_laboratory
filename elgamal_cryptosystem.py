#elgamal system
import gmpy2
import random
import Crypto.Util.number as number
import hashlib
from Crypto.Hash import SHA256

def primes(n):
    p = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            p.append(d)  
            n //= d
        d += 1
    if n > 1:
       p.append(n)
    return p

def phi(n):
	arr = primes(n)
	f = 1
	for t in arr:
		f*=(t-1) 
	return f

def gcd(a, b):
    while(b>0):
        temp = a%b
        a = b
        b = temp
    return a

def order(a,n):
	k = 1
	while(pow(a,k,n) != 1):
		k+=1
	return k

def key_generator():
	p = number.getPrime(1024)
	print p
	q = 91
	while True:
		r = number.getPrime(100)
		euler_n = p-1
		print r
		if(order(r,p) == euler_n):
			e1 = r
			break
	print e1
	# while True:
	# 	d = random.randint(q,p-1)
	# 	if(gcd(d,p)== 1):
	# 		break

	# e2 = powmod(e1,d,p)
	# e1, e2 and p are public keys
	# # d is the private key
	# return [e1,e2,p,d]

if __name__=="__main__":
    key_generator()
	#print [e1,e2,p,d]