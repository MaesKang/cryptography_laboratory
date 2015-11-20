# pollards rho method of factorization
# sample input
#  n = 57247159
#  B = 8
def gcd(a, b):
    while(b>0):
        temp = a%b
        a = b
        b = temp
    return a

def f(x):
	return x*x+1

def pollard_rho(n,B):
	x = 2
	y = 2
	p = 1
	while p==1:
		x = f(x)%n
		y = f(f(y)%n)%n
		p = gcd(x-y,n)
	print p
	if p == n:
		print "Failure"

if __name__=="__main__":
	n = int(input("Enter the number to be factorized : "))
	B = int(input("Enter the Bound : "))
	pollard_rho(n,B)