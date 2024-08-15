"""
Aims of different structural patterns:

Adapter -
Aims to make two incompatible interfaces compatible.
example: XML to JSON converter

Bridge -
Aims to separate abstraction from implementation.
Useful when you have multiple variations or dimensions in your software that can change independently of each other.
Example: Drawing different shapes[rectangle, square, circle,.....] and rendering modes[print, display,.....].

Fly weight -
aims to minimize memory usage or computational expenses
Example: Text editor where the same font is used multiple times.

Composite -
Aims to compose objects into tree structures to represent part-whole hierarchies.
Example: Simple to complex metrics in a dashboard.

Decorator -
Aims to add behavior to individual objects, either statically or dynamically.
Example: Adding new features to a text editor, without affecting the existing features.

Facade -
Aims to provide a simplified interface to a complex system.
Example: Home entertainment system with TV, sound system, gaming console, and smart lighting.

Proxy -
Aims to provide a placeholder for another object to control access to it.
Example: A proxy server that acts as an intermediary between clients and servers. Django Models.
"""