def gcd(x,y):
    while(x%y!=0):
        z=y
        y=x%y
        x=z
    return y
a=int(input("Enter two numbers for GCD\n"))
b=int(input())
print("The GCD of %s and %s is %s"%(a,b,gcd(a,b)))