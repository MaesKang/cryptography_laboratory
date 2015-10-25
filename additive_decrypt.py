#breaking additive cipher 
#answer in 19th iteration NOTVERYSECURE

t = 'UVACLYFZLJBYL'
l = 0
for i in range(1,26):
	temp = ''
	for j in range(0,len(t)):
		temp += chr(((ord(t[j])-ord('A')+i)%26+ord('A')))
	print("Iteration No. {0}".format(i))
	print(temp)


