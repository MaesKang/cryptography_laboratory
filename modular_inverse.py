def ReversePrime(a,n):
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
		r2 = r
		t = int(t1 - t2*q)
		t1 = t2
		t2 = t
	if(t1  < 0):
		return n+t1
	else:
		return t1
