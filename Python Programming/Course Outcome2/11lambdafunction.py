print("What do you want to find\n")
print("\n1.Area of Square\n2.Area of Rectangle\n3.Area of Triangle\n")
n=int(input("Enter the option\n"))
if n==1:
    area=lambda a:a**2
    a=int(input("Enter the value of one side of square"))
    print("The Area of Square = "+str(area(a)))
elif n==2:
    area=lambda a,b:a*b
    a=int(input("Enter length and breadth of Rectangle"))
    b=int(input())
    print("The area of rectangle = "+str(area(a,b)))
elif n==3:
    area=lambda a,h:(1/2)*a*h
    a=int(input("Enter lengths of height and base of Triangle"))
    h=int(input())
    print("The Area of Triangle = "+str(area(a,h)))
else:
    print("Entered wrong option")
