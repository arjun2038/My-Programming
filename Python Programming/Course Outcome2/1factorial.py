def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=i*fact
    return fact
n=int(input("Enter the value for factorial need to find\n"))
if n==0:
    print("The factorial 0! = 1")
else:
    print("The factorial "+str(n)+"! = "+str(factorial(n)))