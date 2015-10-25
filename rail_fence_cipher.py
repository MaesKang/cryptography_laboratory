#encryption using rail fence cipher 
# eg . 
#  text -> MEET ME AT PARK
# encryption in zig-zag order
#     M   E   M   T   A   K
#	  \ / \ / \ / \ / \ / 
#       E	  T   A   P   R
# encrypted text as -> MEMTAKETAPR
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


#decryption of the rail fence cipher	
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
