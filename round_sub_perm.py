# Assignment 7 
# Substitution + Permutation Rounds
# Compiler : Python 3.x


sbox = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

pbox = [0, 3, 4, 6, 2, 5, 1, 7]

reverse_sbox = [14, 3, 4, 8, 1, 12, 10, 15, 7, 13, 9, 6, 11, 2, 0, 5]

reverse_pbox = [0, 6, 4, 1, 2, 5, 3, 7]

round_key = "10010111010100010101000100101000"

def permutation(input_text):
	text = ''
	for i in range(8):
		text += str(input_text[pbox[i]])
	return text

def substitution(input_text):
	text1 = int(input_text[0:4],2)
	text2 = int(input_text[4:],2)
	text1 = str(format(sbox[text1],'#06b'))[2:]
	text2 = str(format(sbox[text2],'#06b'))[2:]
	return text1+text2
	
	
def rounding(r,text_input,round_key):
	text = ''
	for i in range(8):
		text += str(int(text_input[i])^int(round_key[i]))
	print("XOR Operated Text  : ",end='')
	print(text)
	text = substitution(text)
	print("Substituted Text   : ",end='')
	print(text)
	text = permutation(text)
	print("Permuted Text      : ",end='')
	print(text)
	print("Round {0} ends...".format(r+1), end='')
	print("\n")
	return text

def encryption():
	plain_text = "10101010"
	print("Encryption :")
	print("Plain Text  : ",end='')
	print(plain_text)
	print()
	print()
	t = plain_text
	for i in range(4): 
		print("Round #{0} key       : {1}".format(i+1,round_key[8*i:8*i+8]))
		if i<3 :	
			t = rounding(i,t,round_key[8*i:8*i+8])
		elif i == 3:
			text = ''
			round_key_last = round_key[8*i:8*i+8]
			print(round_key_last)
			for i in range(8):
				text += str(int(t[i])^int(round_key_last[i]))
			print("XOR Operated Text  : ",end='')
			print(text)
			text = substitution(text)
			print("Substituted Text   : ",end='')
			print(text)
			print("Round 4 ends ...")
			t = text
	return t

def reverse_permutation(cipher_text):
	text = ''
	for i in range(8):
		text += str(cipher_text[reverse_pbox[i]])
	return text


def reverse_substitution(cipher_text):
	text1 = int(cipher_text[0:4],2)
	text2 = int(cipher_text[4:],2)
	text1 = str(format(reverse_sbox[text1],'#06b'))[2:]
	text2 = str(format(reverse_sbox[text2],'#06b'))[2:]
	return text1+text2

def reverse_round(r,text,r_key):
	if(r!=3):
		text = reverse_permutation(text)
		print("Rev Permuted Text  : ",end='')
		print(text)

	text = reverse_substitution(text)
	print("Rev Substitute Text: ",end='')
	print(text)
	t = ''
	for i in range(8):
		t += str(int(text[i])^int(r_key[i]))
	print("XOR'ed Text        : ",end='')
	print(t)
	text = t

	print("Round {0} ends... ".format(r+1), end='')
	print()
	print()
	return text


def decryption(cipher_text):
	print("CipherText : ",end='')
	print(cipher_text)
	print("\n")
	t = cipher_text
	for i in range(4):
		print("Round #{0} key       : {1}".format(i+1,round_key[8*(3-i):8*(3-i)+8]))
		t = reverse_round(3-i,t,round_key[8*(3-i):8*(3-i)+8])

if __name__=="__main__":
	t = encryption()
	print()
	print("Encryption complete")

	print()
	decryption(t)
	print()
	print("Decryption complete")