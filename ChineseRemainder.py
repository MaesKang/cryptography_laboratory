def GCD(a, b):
    r1 = a
    r2 = b

    while(r2 > 0):
        q = r1/r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
    return r1



def ExGCD(a, b):
    r1 = a
    r2 = b
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while(r2 > 0):
        q = r1/r2

        r = r1 - q * r2
        r1 = r2
        r2 = r

        s = s1 - q * s2
        s1 = s2
        s2 = s

        t = t1 - q * t2
        t1 = t2
        t2 = t
        
    return (r1, s1, t1)

def MulInv(n, b):
    if(GCD(n, b) == 1):
        t = ExGCD(n, b)
        if(t[2]< 0):
            return t[2]%n
        return t[2]
    else:
        print "Multiplicative Inverse doesn't exists."


def ChineseRemainder():
    n = int(raw_input("Enter number of equations: "))
    Moduli = []
    Constants = []
    M = 1
    for i in range(n):
        print "Enter Constant & Modulus for Equation " +str(i + 1)+ ": "
        num = int(raw_input())
        Constants.append(num)
        num = int(raw_input())
        M = num * M
        Moduli.append(num)
    Mi = 0
    Miinv = 0
    sum = 0
    for i in range(n):
        Mi = M/Moduli[i]
        Miinv = MulInv(Moduli[i], Mi)
        sum = sum + (Constants[i] * Mi * Miinv)
        
    x = sum % M
    
    return x
        
