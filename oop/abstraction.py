# Abstraction using ABC module

from abc import ABC, abstractmethod  # import abstract base class tools

class Shape(ABC):  # abstract class
    
    @abstractmethod
    def area(self):
        pass  # no implementation (force child class to define it)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):  # must implement abstract method
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Using abstraction
r = Rectangle(5, 4)
c = Circle(3)

print("Rectangle Area:", r.area())
print("Circle Area:", c.area())
