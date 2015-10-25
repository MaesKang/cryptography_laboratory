# Cryptanalysis and known plain text attack demonstration on a Psuedo Random number generator
# Psuedo Random function  Sj = (A.Sj-1 + B) mod m 
# Author  : Suman Sahu
# Roll No : 712CS2151
# Program to be compiled with Python 3.x

# In this code bit size is 5

# For ENCRYPTION
# TEXT : 'sum' where each alphabet is considered in size of 
# A = 1 and B = 1 and S0 = '00001'

#Multiplicative inverse
def multiplicative_inverse(a,n):
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
	if(r1==1):
		binv = t1;
		if(t1  < 0):
			return n+t1
		else:
			return t1
	else:
		return -1


#Encryption algorithm
def encrypt(s0, m, a, b, plain_text):
	plain_bit_stream = []
	for i in range(len(plain_text)):
		plain_bit_stream.append(str(format(ord(plain_text[i])-ord('a') ,'#07b'))[2:])
	print("PlainText bit Stream    : ",end = '')
	print(plain_bit_stream)	
	cipher_stream = []
	psuedo_random_stream = []
	for i in range(len(plain_text)):
		s_bit_stream = str(format(s0,'#07b'))[2:]
		psuedo_random_stream.append(s_bit_stream)
		temp =''
		for j in range(5):
			temp+=str(int(s_bit_stream[j])^int(plain_bit_stream[i][j]))
		cipher_stream.append(temp)
		s0 = (a*s0 + b)%26
	print("PsuedoRandom bit Stream : ",end = '')
	print(psuedo_random_stream)
	print("CipherText bit Stream   : ",end = '')
	print(cipher_stream)
	return [cipher_stream,plain_bit_stream]

#Given known CipherText and PlainText we have to find values for  A and B by cryptanalysis
def decrypt(known_plain_stream, know_cipher_stream):
	s0 = int(known_plain_stream[0],2)^int(know_cipher_stream[0],2)
	s1 = int(known_plain_stream[1],2)^int(know_cipher_stream[1],2)
	s2 = int(known_plain_stream[2],2)^int(know_cipher_stream[2],2)
	
	print("------- Decryption : Cryptanalysis Known PlainText Attack -------------- ")
	print("Value of s0 , s1 , s2 : ", end='')
	print([s0,s1,s2])
	a = ((s2 - s1)*multiplicative_inverse(s1 - s0, 26))%26
	b = s1 - a*s0
	print("A and B :",end='')
	print([a,b])

if __name__=="__main__":
	[known_cipher_stream, known_plain_stream] = encrypt(1,26,1,1,"sum")
	decrypt(known_plain_stream, known_cipher_stream)