import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
r=float(input("Enter the radius of the circle: "))
w=float(input("Enter the width of the rectangle: "))
h=float(input("Enter the hight of the rectangle: "))
circle = Circle(r)
print(f"Area of the circle: {circle.area():.2f}")
rectangle = Rectangle(w, h)
print(f"Area of the rectangle: {rectangle.area()}")