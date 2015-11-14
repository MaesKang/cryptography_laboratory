def GCD(a, b):
    r1 = a
    r2 = b

    while(r2 > 0):
        q = r1/r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
    return r1
