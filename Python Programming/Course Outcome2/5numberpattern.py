n=int(input("Enter the size N= "))
for i in range(1,n+1):
    for j in range(1,n+1):
        x=i*j
        if j<=i:
            print(str(x)+" ",end="")
        else:
            print(" ",end="")
        x=x*j
    print("\n")