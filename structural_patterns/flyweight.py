"""
The Flyweight Design Pattern is a structural pattern that aims to minimize memory usage or computational expenses
by sharing as much as possible with related objects. It is particularly useful when you have a large number of similar
objects that can be effectively shared to reduce memory consumption.

Example Problem:
Imagine you are developing a word processing application, and you need to represent individual characters on the screen.
Each character (e.g., letters, digits, punctuation) has its own properties, such as font, size, and color.
If you create a separate object for each character on the screen, you would quickly consume a lot of memory.

Solution with the Flyweight Pattern:
The Flyweight Pattern suggests that you separate the intrinsic state (shared and immutable) from the extrinsic state
(context-specific and mutable) of objects. In our example, the intrinsic state represents the properties shared among
characters (e.g. font, size), while the extrinsic state represents the context-specific properties
(e.g. position on the screen)
"""
from typing import Dict, Tuple


class Character:
    def __init__(self, char, font, size, color):
        self.char = char
        self.font = font
        self.size = size
        self.color = color

    def display(self, x, y):
        print(f'Displaying {self.char} at position ({x}, {y})')


class CharacterFactory:
    def __init__(self):
        self.characters: Dict[Tuple, Character] = {}

    def get_character(self, char, font, size, color):
        key = (char, font, size, color)
        if char not in self.characters:
            self.characters[key] = Character(char, font, size, color)
        return self.characters[key]


class WordProcessor:
    def __init__(self):
        self.factory = CharacterFactory()
        self.characters = []

    def add_character(self, char, font, size, color, x, y):
        self.characters.append(self.factory.get_character(char, font, size, color).display(x, y))


if __name__ == '__main__':
    wp = WordProcessor()
    wp.add_character('H', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('e', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('l', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('l', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('o', 'Arial', 12, 'blue', 0, 0)
    wp.add_character(' ', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('W', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('o', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('r', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('l', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('d', 'Arial', 12, 'blue', 0, 0)
    wp.add_character('!', 'Arial', 12, 'blue', 0, 0)
