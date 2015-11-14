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


        
