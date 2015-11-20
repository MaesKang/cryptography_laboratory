# RSA crypto-system
import gmpy2
import random
import Crypto.Util.number as number
import hashlib
from Crypto.Hash import SHA256

# greatest comman divisor
def gcd(a, b):
    while(b>0):
        temp = a%b
        a = b
        b = temp
    return a

# Multiplicative Inverse
def multiplicative_inverse(a,n):
	r = 0
	r1 = n
	r2 = a
	t1 = 0
	t2 = 1
	t = 0
	while(r2>0):
		q = int(r1/r2)
		r = int(r1 - r2*q)
		r1 = r2
		# print("r cond :",end="")
		# print(r1,r2)
		r2 = r
		t = int(t1 - t2*q)
		t1 = t2
		t2 = t
		# print("t cond :",end="")
		# print(t1,t2)
		
	if(r1==1):
		binv = t1;
		if(t1  < 0):
			return n+t1
		else:
			return t1
	else:
		return -1

def support():
	p = number.getPrime(100)
	q = number.getPrime(100)
	n = p*q;
	euler_n = (p-1)*(q-1)
	while True:
		e = random.randint(2,euler_n)
		if(gcd(e,euler_n) == 1):
			d = multiplicative_inverse(e,euler_n)
			break
	return [e,d,n]



def encryption(M,e,n):
	C = pow(M,e,n)
	return C

def decryption(C,d,n):
	M = pow(C,d,n)
	return M

if __name__=="__main__":
	[e,d,n] = support() 
	print("n = {0} \ne = {1} \nd = {2}\n".format(n,e,d))
	M = int(input("Enter number : "))
	C = encryption(M,e,n)
	print "Encrypted Text : ",
	print C
	M = decryption(C,d,n)
	print "Decrypted Text : ",
	print M