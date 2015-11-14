# miller robin test for primality
import random

def break_number(n):
	r = 0
	while(n%2==0):
		r+=1
		n/=2
	return [r,n]

n = int(input("Enter a number (>3) :"))
k = int(input("Enter k to determine accuracy : "))
[r,d] = break_number(n-1)
for i in range(k):
	trig = 1
	a = random.randint(2,n-2)
	x = (a**d)%n
	if x==1 or x==n-1:
		continue
	for j in range(r-1):
		x = (x**2)%n
		if x == 1 :
			print "Composite"
			exit()
		if x==n-1:
			trig = 0
			break
	if trig == 0:
		continue
	print "Composite"
print "Probably a Prime"