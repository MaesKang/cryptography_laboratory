# fermats test for primality
import random

n = int(input("Enter the number : "))
count = 0
for i in range(50):
	a = random.randint(2,n)
	if((a**(n-1))%n==1):
		count+=1
print "Probabilty of number to be prime is :",
print count*2,
print "%"