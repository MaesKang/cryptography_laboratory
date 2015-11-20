#Fermats Factorization method .. works for perfect squares only

def fermats_factorization(n):
	x = pow(n,0.5)
	#x+=1
	while(x < n):
		#print [x*x,n]
		w = (x*x) - n
		if(pow(w,0.5) - int(pow(w,0.5)) == 0):
			y = pow(w,0.5)
			a = x+y
			b = x-y
			print [a,b]
		x = x+1

def main():
	n = int(input("Enter number to be factorized : "))
	fermats_factorization(n)

if __name__=="__main__":
	main()