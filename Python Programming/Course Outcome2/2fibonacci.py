n=int(input("How many fibonacci numbers to print?\n"))
f1=0
f2=1
print("The first "+str(n)+" fibonacci numbers are\n")
for i in range(n):
    if i==0:
        print(str(f1),end=",")
    if i==1:
        print(str(f2),end=",")
    if i>1:
        f3=f1+f2
        print(str(f3),end=",")
        f1=f2
        f2=f3