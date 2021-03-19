class rectangle:
    __length=0
    __breadth=0
    __area=0
    def __init__(self,l,w):
        self.__length=l
        self.__width=w
    def area(self):
        self.__area=self.__length*self.__width
    def __gt__(self,other):
        if(self.__area>other.__area):
            return True
        else:
            return False
ob1=rectangle(5,4)
ob1.area()
ob2=rectangle(6,7)
ob2.area()
if(ob1>ob2):
    print("object1 is greater than object2")
else:
    print("object2 is greater than object1")
