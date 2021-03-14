class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        a=self.length*self.breadth
        return a
    def premeter(self):
        b=2*(self.length+self.breadth)
        return b

    
a=int(input("Enter the length of the 1st rectangle:"))
b=int(input("Enter the breadth of the 1st rectangle:"))
c=int(input("Enter the length of the 2nd rectangle:"))
d=int(input("Enter the breadth of the 2nd rectangle:"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
print("Area of rectangle:",obj1.area(),"And","Perimeter of rectangle:",obj1.premeter())
print("Area of rectangle:",obj2.area(),"And","Perimeter of rectangle:",obj2.premeter())

if obj1.area() == obj2.area():
     print("Both  rectangle have same area ",obj1.area())
elif obj1.area() > obj2.area():
     print("First rectangle is greater ",obj1.area())
else:
    print("Second rectangle is greater ",obj2.area())
