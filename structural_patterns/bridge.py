"""
Problem:
The Bridge Pattern is a structural design pattern that separates an object's abstraction from its implementation.
It allows you to create two different hierarchies and change them independently.
This pattern is particularly useful when you have multiple variations or dimensions in your software that can change
independently of each other.

Real-life Example Problem:
Let's consider a real-life problem in a drawing application. You have different shapes to draw, such as circles and
squares, and you also want to support different rendering modes, such as rendering to the screen or printing to paper.
Without the Bridge Pattern, you might end up with a complex hierarchy of classes like this:
"""


class CircleScreen:
    def draw(self):
        print("Drawing a circle on the screen")


class CirclePrinter:
    def draw(self):
        print("Printing a circle on paper")


class SquareScreen:
    def draw(self):
        print("Drawing a square on the screen")


class SquarePrinter:
    def draw(self):
        print("Printing a square on paper")


"""
However, this approach leads to a combinatorial explosion of classes as you add more shapes and rendering modes. 
It becomes hard to maintain and extend the code.

Solution with the Bridge Pattern:
The Bridge Pattern helps to separate the abstraction (shapes) from the implementation (rendering modes). 
It introduces two separate hierarchies, allowing you to change them independently. 
Here's how you can use the Bridge Pattern to solve the problem:
"""


class Renderer:
    def render(self):
        pass


class ScreenRenderer(Renderer):
    def render(self):
        return " on the screen"


class PrinterRenderer(Renderer):
    def render(self):
        return " on paper"


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        raise NotImplementedError


class Circle(Shape):
    def draw(self):
        print("Drawing a circle" + self.renderer.render())


class Square(Shape):
    def draw(self):
        print("Drawing a square" + self.renderer.render())


if __name__ == "__main__":
    screen_renderer = ScreenRenderer()
    printer_renderer = PrinterRenderer()

    shapes = [Circle(screen_renderer), Circle(printer_renderer), Square(screen_renderer), Square(printer_renderer)]
    for shape in shapes:
        shape.draw()
