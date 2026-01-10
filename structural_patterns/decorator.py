"""
The Decorator Design Pattern is a structural pattern that allows behavior to be added to individual objects,
either statically or dynamically, without affecting the behavior of other objects from the same class.
It's often used to extend the functionality of classes in a flexible and reusable way.

Adapter changes the behaviour but decorator adds/enhances new behaviour.
"""
from abc import ABC, abstractmethod


# Component interface or base class
class TextComponent(ABC):
    @abstractmethod
    def display(self):
        pass


# Concrete component class
class PlainText(TextComponent):
    def __init__(self, content: str):
        self._content = content

    def display(self):
        return self._content


# Decorator class
class TextDecorator(TextComponent):
    def __init__(self, text_component: TextComponent):
        self._text_component = text_component

    @abstractmethod
    def display(self):
        pass


# Concrete decorator classes for text formatting
class BoldDecorator(TextDecorator):
    def display(self):
        return "<b>" + self._text_component.display() + "</b>"


class ItalicDecorator(TextDecorator):
    def display(self):
        return "<i>" + self._text_component.display() + "</i>"


class ColorDecorator(TextDecorator):
    def __init__(self, text_component: TextComponent, color: str):
        super().__init__(text_component)
        self._color = color

    def display(self):
        return f'<span style="color:{self._color};">{self._text_component.display()}</span>'


# Usage
if __name__ == "__main__":
    plain_text = PlainText("Hello, World!")

    bold_text = BoldDecorator(plain_text)
    italic_and_color_text = ColorDecorator(ItalicDecorator(plain_text), "blue")

    print("Plain text:", plain_text.display())  # Output: Plain text: Hello, World!
    print("Bold text:", bold_text.display())  # Output: Bold text: <b>Hello, World!</b>
    print("Italic and colored text:", italic_and_color_text.display())
    # Output: Italic and colored text: <span style="color:blue;"><i>Hello, World!</i></span>


# One more example
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    
class SimpleCoffee(Coffee):
    def cost(self):
        return 50
        

class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 30

class SugarDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost() + 10

if __name__ == "__main__":
    coffee = SimpleCoffee()
    add_milk = MilkDecorator(coffee)
    add_sugar = SugarDecorator(add_milk)

    print(add_sugar.cost())
