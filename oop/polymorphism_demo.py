import math

class Shape:
    def area(self):
        """This method should be overridden by derived classes."""
        raise NotImplementedError("The area method must be overridden in a subclass.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Initialize the Circle with radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * (self.radius ** 2)
