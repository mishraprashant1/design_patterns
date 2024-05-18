"""
Abstractions should not depend upon details. Details should depend upon abstractions.

The Dependency Inversion Principle suggests that high-level modules should not depend on low-level modules. Both should
depend on abstractions. Additionally, abstractions should not depend on details. Details should depend on abstractions.

By applying the Dependency Inversion Principle, you can create a more flexible and maintainable software architecture by
decoupling high-level modules from low-level modules and allowing them to depend on abstractions rather than concrete
implementations.

Benefits of the Dependency Inversion Principle:

1. Decoupling: The Dependency Inversion Principle helps to decouple high-level modules from low-level modules, reducing

2. Flexibility: By depending on abstractions rather than concrete implementations, the Dependency Inversion Principle

3. Maintainability: The Dependency Inversion Principle promotes maintainable code by reducing dependencies between

4. Re-usability: By decoupling high-level modules from low-level modules, the Dependency Inversion Principle helps to

5. Testability: The Dependency Inversion Principle makes it easier to test high-level modules by allowing you to replace

By following the Dependency Inversion Principle, you can create more flexible, maintainable, and testable software systems
that are easier to extend and modify.
"""

# Dependency Inversion Principle Example

from abc import ABC, abstractmethod


class BadPaymentProcessor:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")


class BadPaymentService:
    def __init__(self):
        self.payment_processor = BadPaymentProcessor()

    def process_payment(self, amount):
        self.payment_processor.process_payment(amount)


# Client code
bad_payment_service = BadPaymentService()
bad_payment_service.process_payment(100)

# Output:
# Processing payment of $100

"""
Above is a bad example of the Dependency Inversion Principle because the BadPaymentService class depends directly on the
BadPaymentProcessor class, violating the principle that high-level modules should not depend on low-level modules.

Refactored Example:
"""


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")


class DigitalWalletProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing digital wallet payment of ${amount}")


class PaymentService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def process_payment(self, amount):
        self.payment_processor.process_payment(amount)


# Client code
credit_card_processor = CreditCardProcessor()
payment_service = PaymentService(credit_card_processor)
payment_service.process_payment(100)

# Output:
# Processing credit card payment of $100

"""
In this refactored example, the PaymentService class depends on the PaymentProcessor interface, which is an abstraction.
This follows the Dependency Inversion Principle by ensuring that high-level modules depend on abstractions rather than
concrete implementations. This makes the code more flexible, maintainable, and testable.

You can easily swap out the payment processor implementation without modifying the PaymentService class, allowing you to
process payments using different payment methods without changing existing code.
"""
