# shift cipher
t = str(input("Enter plain Text : "))
t = t.upper()
i = int(input("Enter the shift Index : "))
temp = ''
for j in range(len(t)):
	temp += chr(((ord(t[j])-ord('A')+i)%26+ord('A')))
print temp