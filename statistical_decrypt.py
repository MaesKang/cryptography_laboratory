#statistical attack
t = 'XLILSYWIMWRSAJSVWEPIJSVJSYVQMPPMSRHSPPEVWMXMWASVXLQSVILYVVCFIJSVIXLIWIPPIVVIGIMZIWQSVISJJIVW'
ch = 'A'
count = []
for i in range(ord('A'),ord('Z')+1):
	count[i-ord('A')] = 
temp = 0
if(ord(ch) < ord('E')):
	temp = ord(ch)+26-ord('E')
else:
	temp = ord(ch) - ord('E')
	
final = ''  
for j in range(0,len(t)):
	final += chr(((ord(t[j])-ord('A')+temp)%26+ord('A')))
print(final)
