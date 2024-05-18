"""

Subtypes must be substitutable for their base types.

The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its
subclasses without affecting the correctness of the program.

In other words, a subclass should be substitutable for its superclass without changing the behavior of the program. This
principle ensures that the derived classes adhere to the contract specified by the base class and maintain the expected
behavior.

Violating the Liskov Substitution Principle can lead to unexpected behavior and errors in the program. By following this
principle, you can create more flexible and maintainable code that is easier to extend and modify.

Example:

Consider a Rectangle class with width and height properties and an area method that calculates the area of the rectangle.
Now, let's create a Square class that inherits from the Rectangle class and overrides the set_width and set_height methods
to ensure that the width and height are always equal.

If the Square class violates the Liskov Substitution Principle, it may lead to unexpected behavior when substituting a
Square object for a Rectangle object in the program.

To adhere to the Liskov Substitution Principle, the Square class should be a valid subtype of the Rectangle class, meaning
that it should behave like a Rectangle in all contexts where a Rectangle is expected.

Let's see an example of the Liskov Substitution Principle in action:
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def __str__(self):
        return f"Square(side={self.width})"


def get_area(rectangle):
    rectangle.set_width(5)
    rectangle.set_height(4)
    return rectangle.area()


if __name__ == "__main__":
    rectangle = Rectangle(0, 0)
    square = Square(0, 0)

    print(get_area(rectangle))  # Output: 20
    print(get_area(square))  # Output: 16

    print(rectangle)  # Output: Rectangle(width=5, height=4)
    print(square)  # Output: Square(side=5)

"""
In this example, we have a Rectangle class with width and height properties and an area method that calculates the area
of the rectangle. We also have a Square class that inherits from the Rectangle class and overrides the set_width and
set_height methods to ensure that the width and height are always equal.

The get_area function takes a Rectangle object as an argument, sets its width and height to 5 and 4, respectively, and
returns the area of the rectangle. When we pass a Rectangle object to the get_area function, it correctly calculates the
area as 20.

However, when we pass a Square object to the get_area function, it sets the width and height to 5 and 4, respectively,
instead of keeping them equal. This violates the Liskov Substitution Principle because the Square class does not behave
like a Rectangle in all contexts where a Rectangle is expected.

By adhering to the Liskov Substitution Principle, we can ensure that subtypes can be substituted for their base types
without affecting the correctness of the program. This principle helps create more flexible and maintainable code that
is easier to extend and modify.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

    def __str__(self):
        return f"Square(side={self.side})"


def get_area(shape):
    if isinstance(shape, Shape):
        return shape.get_area()
    else:
        raise ValueError("Invalid shape object")


if __name__ == "__main__":
    rectangle = Rectangle(0, 0)
    square = Square(0)

    print(get_area(rectangle))  # Output: 0
    print(get_area(square))  # Output: 0

    rectangle.set_width(5)
    rectangle.set_height(4)
    square.set_side(5)

    print(get_area(rectangle))  # Output: 20
    print(get_area(square))  # Output: 25

    print(rectangle)  # Output: Rectangle(width=5, height=4)
    print(square)  # Output: Square(side=5)

"""
In this example, we have defined a Shape interface with an abstract method get_area that returns the area of the shape.
The Rectangle and Square classes implement the Shape interface and provide concrete implementations of the get_area
method.

The get_area function takes a Shape object as an argument and calls the get_area method on the object to calculate the
area of the shape. By using the Shape interface, we can ensure that both Rectangle and Square objects can be treated
uniformly based on their common behavior.

When we pass a Rectangle object to the get_area function, it correctly calculates the area as 20 by setting the width 
and height of the rectangle to 5 and 4, respectively. Similarly, when we pass a Square object to the get_area function, 
it calculates the area as 25 by setting the side of the square to 5.

By adhering to the Liskov Substitution Principle and using interfaces to define common behavior, we can create more
flexible and maintainable code that allows for easy substitution of objects without affecting the correctness of the
program.
"""
