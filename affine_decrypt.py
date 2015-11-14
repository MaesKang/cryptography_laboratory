
# Decrypting the affine cipher

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

def decrypt(s,k,n):
    t = ''
    for i in range(0,len(s)):
        if(multiplicative_inverse(k,26) != -1):
            t = t + str(chr((((ord(s[i])-ord('A')) - n)*multiplicative_inverse(k,26))%26+ord('A')))
        else:
            print 'Multiplicative Inverse doesnt Exist'
            exit()
    return t

s = str(raw_input("Cipher Text:"))
s = s.upper()
c_text = s 
p_box = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075, 0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]

p_s = []
for x in p_box:
    k = p_box.index(max(p_box))
    p_s.append(k)
    p_box[k] = 0.0

c_no = []
ch = map(chr, range(ord('A'), ord('Z')))
for x in ch:
    c_no.append(s.count(x))
print c_no

m1 = c_no.index(max(c_no))
c_no[m1] = 0;
m2 = c_no.index(max(c_no))

a = 1
for x in p_s:
    b = (m1 - x*a)%26
    print("A = {0}, B = {1} : {2}".format(a,b,decrypt(s, a, b)))
