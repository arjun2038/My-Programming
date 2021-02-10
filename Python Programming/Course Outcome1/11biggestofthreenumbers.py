a = int(input("Enter three numbers to compare\n"))
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print(str(a) + " is the biggest number")
    elif c>b:
        print(str(c) + " is the biggest number")
elif b > c:
    print(str(b) + " is the biggest number")
elif(c>b):
    print(str(c) + " is the biggest number")


