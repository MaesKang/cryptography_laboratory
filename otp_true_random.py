# True random number generator
# Author  : Suman Sahu
# Roll No : 712CS2151
# Program to be compiled with Python 3.x

import random

#encryption
def encrypt():
	t = str(input("Enter the text : "))
	input_text  = ''.join(str(format(ord(i),'#010b'))[2:] for i in t)
	print("Input Text : ",end='')
	print(input_text)
	#generate random sequence of len(input_text) bits
	otp = []
	for i in range(len(input_text)):
		otp.append(int(round(random.random())))
	print("OTP        : ",end='')
	print(''.join( str(i) for i in otp)) 
	#XORing for cipher stream
	cipher_stream = [] 
	for i in range(len(input_text)):
		cipher_stream.append(int(input_text[i])^otp[i])
	cipher_text = ''.join(str(i) for i in cipher_stream)
	print("Cipher Text: ",end='')
	print(cipher_text)
	return [cipher_stream,otp]

#decryption
def decrypt(cipher_stream,otp):
	plain_stream = []
	for i in range(len(cipher_stream)):
		plain_stream.append(cipher_stream[i]^otp[i])
	plain_bit_text = ''.join(str(i) for i in plain_stream)
	chunks , chunks_size = len(plain_bit_text) , 8
	chunk_bits = [ plain_bit_text[i:i+chunks_size] for i in range(0, chunks, chunks_size)]
	plain_text = ''.join(str(chr(int(i,2))) for i in chunk_bits)
	print("----- Decryption---------------")
	print("Plain Text : ",end='')
	print(plain_text)


if __name__ == "__main__":
	[cipher_stream,otp] = encrypt()
	decrypt(cipher_stream,otp)