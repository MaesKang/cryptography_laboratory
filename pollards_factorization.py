# Pollards p-1 factorization method
# sample input
#  n = 57247159
#  B = 8
def gcd(a, b):
    while(b>0):
        temp = a%b
        a = b
        b = temp
    return a

def pollards(n,B):
	a = 2
	e = 2
	while(e <= B):
		a = pow(a,e,n)
		e = e + 1
	p = gcd(a-1,n)
	if 1 < p and p < n :
		print p
	else:
		print "failure"

if __name__ == "__main__":
	n = int(input("Enter a number to be factorized : "))
	B = int(input("Enter the Bound : "))
	pollards(n,B)