# primitive roots
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

def primitive_roots(n):
	euler_n = phi(n)
	print "phi = ",
	print euler_n
	roots = []
	for i in range(2,n):
		if gcd(i,n)==1:
			if(order(i,n) == euler_n):
				roots.append(i)
	return roots

if __name__=="__main__":
	n = int(input("Enter number : "))
	roots = primitive_roots(n)
	print "Primitive roots : ",
	print roots