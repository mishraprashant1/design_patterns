"""
The Composite Design Pattern is a structural pattern used to compose objects into tree structures to represent
part-whole hierarchies. It allows clients to treat individual objects and compositions of objects uniformly.

Real-Life Example Problem:

Imagine you are building a graphical drawing application, and you need to represent complex shapes that can be
composed of smaller shapes, including basic shapes like circles and rectangles, as well as more complex shapes
like groups that contain other shapes or even nested groups.

Without the Composite Pattern, you might create separate classes for each shape and handle groups differently
from individual shapes. This could result in complex and tightly coupled code.

Solution with the Composite Pattern:

The Composite Pattern suggests that you create a common interface or base class for all shapes, both primitive and
composite. Each shape, including groups, implements this interface, allowing them to be treated uniformly.

Composite means "made up of several individual parts".
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Drawing Circle')


class Rectangle(Shape):
    def draw(self):
        print('Drawing Rectangle')


class CompositeShape(Shape):

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        print('Drawing a Complex Composite Shape')
        for shape in self.shapes:
            shape.draw()


if __name__ == '__main__':
    circle = Circle()
    rectangle = Rectangle()

    complex_shape = CompositeShape()
    complex_shape.add_shape(circle)
    complex_shape.add_shape(circle)
    complex_shape.add_shape(rectangle)

    complex_shape.draw()