# affine cipher

# multiplictive inverse
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
        # print("r cond :",end="")
        # print(r1,r2)
        r2 = r
        t = int(t1 - t2*q)
        t1 = t2
        t2 = t
        # print("t cond :",end="")
        # print(t1,t2)
        
    if(r1==1):
        binv = t1;
        if(t1  < 0):
            return n+t1
        else:
            return t1
    else:
        return -1

def affine_decrypt(t,k,b):
	temp = ''
	for j in range(len(t)):
		temp += chr((((ord(t[j])-ord('A') - b)* multiplicative_inverse(k,26))%26+ord('A')))
	return temp

def affine_encrypt(t,k,b):
	temp = ''
	for j in range(len(t)):
		temp += chr((((ord(t[j])-ord('A'))*k+b)%26+ord('A')))
	return temp

def main():
	t = str(raw_input("Plain Text : "))
	t = t.upper()
	print "Cipher of the form (A*k + b)%26"
	k = int(input("Value of k : "))
	b = int(input("Value of b : "))  
	t = affine_encrypt(t,k,b)
	print "After encryption : "+t
	t = affine_decrypt(t,k,b)
	print "After decryption : "+t

if __name__=="__main__":
	main()