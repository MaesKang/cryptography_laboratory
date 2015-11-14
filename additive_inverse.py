def additive_inverse(x,n):
	if n-x > 0:
		return n-x
	else:
		return (n-x)+n

def main():
	x = int(input("Enter value of x :"))
	n = int(input("Enter value of n :"))
	print("Additive Inverse : {0}".format(additive_inverse(x,n)))

if __name__=="__main__":
	main()