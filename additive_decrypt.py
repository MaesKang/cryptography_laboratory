
# Brute force attack on cipher text

t = str(raw_input("Enter the Cipher Text : "))
t = t.upper()
l = 0
for i in range(1,26):
	temp = ''
	for j in range(0,len(t)):
		temp += chr(((ord(t[j])-ord('A')+i)%26+ord('A')))
	print("Iteration No. {0} : {1} ".format(i, temp))