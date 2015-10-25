def rail_fence_decrypt(s):
	s = s.replace(' ','')
	t = ''
	if(len(s)%2==0):
		for i in range(0,len(s)/2):
			t+=s[i]
			t+=s[len(s)/2+i]
	else:
		for i in range(0,len(s)/2):
			t+=s[i]
			t+=s[len(s)/2+i+1]
		t+=s[len(s)/2]
	return t
		
