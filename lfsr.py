# Linear FeedBack Shift Register
# Author  : Suman Sahu
# Roll No : 712CS2151
# Program to be compiled with Python 3.x


# Given, p3 = 0, p2 = 0, p1 = 1, p0 = 0
# and, Degree (m) = 4
def encrypt(plaintext,seed):
	in_t = ''.join(str(format(ord(i),'#010b'))[2:] for i in plaintext)
	t= ''
	round_keys = []
	for i in range(int(len(in_t)/4)):
		round_keys.append(''.join(str(k) for k in seed))
		t+=str(int(seed[0])^int(in_t[4*i]))
		t+=str(int(seed[1])^int(in_t[4*i+1]))
		t+=str(int(seed[2])^int(in_t[4*i+2]))
		t+=str(int(seed[3])^int(in_t[4*i+3]))
		temp = seed[1]^seed[0]
		seed[0] = seed[1]
		seed[1] = seed[2]
		seed[2] = seed[3]
		seed[3] = temp
	print("Round Keys:",end='')
	print(round_keys)
	print("CipherText:",end='')
	print(t)

if __name__ == "__main__":
	encrypt("su",[0,0,1,1])