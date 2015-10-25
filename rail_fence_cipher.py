def rail_fence(s):
	s = s.replace(' ','')
	t1=''
	t2=''
	for i in range(0,len(s)):
		if(i&1==0):
			t1+=s[i];
		else:
			t2+=s[i];
	return t1+t2
