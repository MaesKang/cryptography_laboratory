# fast exponentiation
# a^b mod n
def fast_exponentiation(a,x,n):
	y = 1
	bin_x = bin(x)[2:]
	for i in range(len(bin_x)):
		if(bin_x[i] == '1'):
			y = (a*y)%n
		a = (a*a)%n
	return [y,a]

if __name__=="__main__":
	a = int(input("Enter A : "))
	x = int(input("Enter X : "))
	n = int(input("Enter N : "))
	print fast_exponentiation(a,x,n)