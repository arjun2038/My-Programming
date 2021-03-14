#Create Rectangle class with attributes length and breadth and methods to find area and
#perimeter. Compare two Rectangle objects by their area
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
rect1=rectangle(1,2)
rect2=rectangle(2,4)
if rect1.area == rect2.area:
    print("Areas of the rectangles are equal")
elif rect1.area < rect2.area:
    print("Area of second triangle is more") 
elif rect1.area > rect2.area:
    print("Area of first triangle is more")     