import graphics.rectangle
from graphics.circle import *
from graphics.graphics3D import cuboid
import graphics.graphics3D.sphere
print("What do you want to find?")
print(
    "1.Area of Rectangle\n2.Perimeter of Rectangle\n3.Area and Perimeter of rectangle\n4.Area of Circle\n5.Perimeter of Circle\n6.Area and Perimeter of Circle\n7.Area of Cuboid\n8.Perimeter of Cuboid\n9.Area and Perimeter of Cuboid\n10.Area of Sphere\n11.Perimeter of Sphere\n12.Area and Perimeter of Sphere")
option = int(input("Enter the Option"))
if option == 1:
    a = int(input("Enter Length and Width"))
    b = int(input())
    print("Area of Rectangle=" + str(Graphics.rectangle.arear(a, b)))
elif option == 2:
    a = int(input("Enter Length and Width"))
    b = int(input())
    print("The Perimeter of the Rectangle=" + str(Graphics.rectangle.perimeterr(a, b)))
elif option == 3:
    a = int(input("Enter Length and Width"))
    b = int(input())
    print("Area of Rectangle=" + str(Graphics.rectangle.arear(a, b)))
    print("The Perimeter of the Rectangle=" + str(Graphics.rectangle.perimeterr(a, b)))
elif option == 4:
    r = int(input("Enter the radius of Circle "))
    print("The Area of Circle=" + str(areacir(r)))
elif option == 5:
    r = int(input("Enter the radius of Circle "))
    print("The Perimeter of the Circle=" + str(perimetercir(r)))
elif option == 6:
    r = int(input("Enter the radius of Circle "))
    print("The Area of Circle=" + str(areacir(r)))
    print("The Perimeter of the Circle=" + str(perimetercir(r)))
elif option == 7:
    a = int(input("Enter the length width hight of cuboid"))
    b=int(input())
    h=int(input())
    print("The Area of Cuboid=" + str(cuboid.areacu(a, b, h)))
elif option==8:
    a = int(input("Enter the length width hight of cuboid"))
    b = int(input())
    h = int(input())
    print("The Perimeter of the Cuboid="+str(cuboid.perimetecu(a,b,h)))
elif option==9:
    a = int(input("Enter the length width hight of cuboid"))
    b=int(input())
    h=int(input())
    print("The Area of Cuboid=" + str(cuboid.areacu(a, b, h)))
    print("The Perimeter of the Cuboid="+str(cuboid.perimetecu(a,b,h)))
elif option==10:
    r=int(input("Enter the radius of Sphere"))
    print("The Area of Sphere="+str(Graphics.Graphics3D.sphere.areasp(r)))
elif option==11:
    r=int(input("Enter the radius of Sphere"))
    print("The Perimeter of Sphere="+str(Graphics.Graphics3D.sphere.perimetesp(r)))
elif option==12:
    r=int(input("Enter the radius of Sphere"))
    print("The Area of Sphere="+str(Graphics.Graphics3D.sphere.areasp(r)))
    print("The Perimeter of Sphere="+str(Graphics.Graphics3D.sphere.perimetesp(r)))
else:
    print("Choose only Above Options")