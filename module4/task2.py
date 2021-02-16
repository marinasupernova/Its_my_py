'''Write a Python class named Rectangle constructed 
by a length and width and a method 
which will compute the area and perimeter of a rectangle.'''

class Rectangle:
    

    def __init__(self,width,length):
        self.width = width
        self.length = length

    def compute_area(self):
        area = self.width * self.length
        return area
        

    def compute_perimeter(self):
        perimeter = 2*(self.length + self.width)
        return perimeter


rct = Rectangle(5, 5)

print(rct.compute_area(), rct.compute_perimeter())