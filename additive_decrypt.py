# Suman Sahu
# additive cipher 

#encryption
def encrypt(text,key):
	text = text.toupper()
	temp = ''
	for i in range(0,len(text)):
		temp += chr(((ord(text[i])-ord('A'))+key)%26+ord('A'))
	return temp

#brute-force approach to break additive cipher
t = 'UVACLYFZLJBYL' # write the givens statement
l = 0
for i in range(1,26):
	temp = ''
	for j in range(0,len(t)):
		temp += chr(((ord(t[j])-ord('A')+i)%26+ord('A')))
	print("Iteration No. {0}".format(i))
	print(temp)




