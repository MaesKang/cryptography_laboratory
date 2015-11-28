# rabin cryptosystem
import gmpy2
import random
import Crypto.Util.number as number

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


def chineese_remainder(a1,b1,p,q):
	M = a1*b1
	M1 = b1
	M2 = a1
	m1 = multiplicative_inverse(M1,a1)
	m2 = multiplicative_inverse(M2,b1)
	x = (p*M1*m1 + q*M2*m2)%M
	return x


def rabin_key_generator():
	while True:
		p = number.getPrime(100)
		if (p+1)%4 == 0:
			break
	while True:
		q = number.getPrime(100)
		if (q+1)%4 == 0:
			break
	n = p*q;
	return [n,p,q]

def encryption(P,n):
	C = pow(P,2,n)
	return C

def decryption(p,q,C):
	a1 = pow(C,(p+1)/4,p)
	a2 = pow(-1*C,(p+1)/4,p)
	b1 = pow(C,(q+1)/4,q)
	b2 = pow(-1*C,(q+1)/4,q)
	P1 = chineese_remainder(a1,b1,p,q)
	P2 = chineese_remainder(a1,b2,p,q)
	P3 = chineese_remainder(a2,b1,p,q)
	P4 = chineese_remainder(a2,b2,p,q)
	return [P1,P2,P3,P4]

if __name__=="__main__":
	[n,p,q] = rabin_key_generator()
	print("n = {0} \np = {1} \nq = {2} \n".format(n,p,q))
	P = int(input("Enter number :"))
	C = encryption(P,n)
	print("Encrypted text : {0}".format(C))
	[P1,P2,P3,P4] = decryption(p,q,C)
	print "Possible decryptions : "
	print P1
	print P2
	print P3
	print P4