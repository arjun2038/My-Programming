class Rectangle:
    def save(self,l,w):
        self.length=l
        self.width=w
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return (self.length+self.width)*2
x=Rectangle()
y=Rectangle()
length1=int(input("Enter the Length of first Rectangle"))
width1=int(input("Enter the Width of First Rectangle"))
length2=int(input("Enter the Length of Second Rectangle"))
width2=int(input("Enter the Width of Second Rectangle"))
x.save(length1,width1)
y.save(length2,width2)
if x.area()>y.area():
    print("Rectangle A has Largest Area")
elif x.area()<y.area():
    print("Rectangle B has Largest Area")
else:
    print("Both Rectangles has same Area")
if x.perimeter()>y.perimeter():
    print("Rectangle A has Largest Perimeter")
elif x.perimeter()<y.perimeter():
    print("Rectangle B has Largest Perimeter")
else:
    print("Both Rectangles has Same Perimeter")