# modular inverse of a matrix
from numpy import *

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

def matrix_cofactor(A):
    return A.I.T * linalg.det(A)

def main():
	n = int(input("Enter dimension of matrix :"))
	A = matrix(input("Enter the matrix : "))
	m = int(input("Enter the mod value : "))
	B = matrix_cofactor(A)
	C = linalg.det(A)
	if(multiplicative_inverse(int(C), m) == -1):
		print "Multiplicative inverse of determinant not found"
		exit()
	C = multiplicative_inverse(int(C), m)
	B = B*C
	for i in range(n):
		for j in range(n):
			B[i,j] = B[i,j] % m
	print "Modular inverse of the matrix is : "
	print B

if __name__=="__main__":
	main()