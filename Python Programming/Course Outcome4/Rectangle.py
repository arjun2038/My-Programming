class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        a = self.length * self.breadth
        return a

    def perimeter(self):
        b = 2 * (self.length + self.breadth)
        return b
a = int(input("Enter the length of the first rectangle:"))
b = int(input("Enter the breadth of the first rectangle:"))
c = int(input("Enter the length of the Second rectangle:"))
d = int(input("Enter the breadth of the Second rectangle:"))
obj1 = rectangle(a, b)
obj2 = rectangle(c, d)
print("Area of First Rectangle:", obj1.area(), "And", "The Perimeter of First rectangle:", obj1.perimeter())
print("Area of Second rectangle:", obj2.area(), "And", "Perimeter of Second rectangle:", obj2.perimeter())

if obj1.area() == obj2.area():
    print("Both  rectangle have same area ", obj1.area())
elif obj1.area() > obj2.area():
    print("First rectangle is greater area", obj1.area())
else:
    print("Second rectangle is greater area ", obj2.area())
