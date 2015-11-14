def GCD(a, b):
    s
    while(b>0):
        temp = a%b
        a = b
        b = temp
    return a

if __name__ == "__main__":
    a = int(raw_input("Enter 1st Number: "))
    b = int(raw_input("Enter 2nd Number: "))
    print "The result is :"+str(GCD(a,b)) 
