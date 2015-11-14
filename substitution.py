# substitution cipher
s_box = 'qwertyuiopasdfghjklzxcvbnm'
s_box = s_box.upper()
t = str(raw_input("Enter the plain text :"))
t = t.upper()
temp = ''
for i in range(len(t)):
	temp+=s_box[ord(t[i])-ord('A')];
print "After Permutation : ",
print temp
t = temp
r_box = 'kxvmcnophqrszyijadlegwbuf'
r_box = r_box.upper()
temp = ''
for i in range(len(t)):
	temp+=r_box[ord(t[i])-ord('A')];
print "After reverse Permutation : ",
print temp