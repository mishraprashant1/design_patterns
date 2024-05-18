"""

Clients should not be forced to depend upon methods that they do not use. Interfaces belong to clients, not to
hierarchies. Here clients refer concrete classes, not abstract classes.

The Interface Segregation Principle suggests that you should split large interfaces into smaller, more specific ones so
that clients only need to know about the methods that are of interest to them. This helps to prevent clients from
depending on methods they do not use.

By applying the Interface Segregation Principle, you can create specific interfaces for each payment method that define
only the methods supported by that method. This allows clients to interact with specific interfaces based on their
requirements, without being forced to implement unnecessary methods.

Benefits of the Interface Segregation Principle:

1. Modularity: The Interface Segregation Principle promotes modularity by breaking down large interfaces into smaller,

2. Flexibility: By defining specific interfaces for each client, the Interface Segregation Principle provides flexibility

3. Re-usability: The Interface Segregation Principle helps to create reusable code by allowing clients to interact with

4. Reduced Dependencies: By creating specific interfaces for each client, the Interface Segregation Principle reduces

5. Improved Maintainability: The Interface Segregation Principle makes it easier to maintain and extend the codebase by

By following the Interface Segregation Principle, you can create more modular, flexible, and maintainable software systems
that are easier to understand and extend.
"""

# Interface Segregation Principle Example

from abc import ABC, abstractmethod


class BadInterfacePrinter(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class BadOldPrinter(BadInterfacePrinter):
    def print(self, document):
        print(f"Printing {document} in black and white...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")


class BadModernPrinter(BadInterfacePrinter):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
The OldPrinter class implements the Printer interface, which defines print, fax, and scan methods. However, the OldPrinter
class does not support faxing or scanning, so it raises NotImplementedError for these methods.

The ModernPrinter class also implements the Printer interface but provides implementations for all three methods: print,
fax, and scan. This violates the Interface Segregation Principle because clients that use the OldPrinter class are forced
to implement methods that they do not need.

To adhere to the Interface Segregation Principle, you can create separate interfaces for printing, faxing, and scanning,
and have the OldPrinter and ModernPrinter classes implement only the interfaces that are relevant to them.

Refactored Example:
"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white...")


class NewPrinter(Printer, Fax, Scanner):
    def print(self, document):
        print(f"Printing {document} in color...")

    def fax(self, document):
        print(f"Faxing {document}...")

    def scan(self, document):
        print(f"Scanning {document}...")


"""
Now Printer, Fax, and Scanner are base classes that provide specific interfaces with a single responsibility each. 
To create OldPrinter, you only inherit the Printer interface. This way, the class won’t have unused methods. 
To create the ModernPrinter class, you need to inherit from all the interfaces. In short, you’ve segregated the Printer 
interface.

This class design allows you to create different machines with different sets of functionalities, making your design 
more flexible and extensible.
"""
