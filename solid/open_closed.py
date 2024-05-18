"""

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

The Open/Closed Principle (OCP) is a fundamental principle in object-oriented design that states that software entities
(classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should
be able to extend the behavior of a software entity without modifying its source code.

The Open/Closed Principle helps to create flexible and maintainable software systems by allowing you to add new features
or behaviors without changing existing code. This principle is often achieved by using abstractions, interfaces, and
polymorphism to decouple the implementation from the client code.

Let's explore the Open/Closed Principle with an example:

Real-Life Example Problem:

Imagine you are developing a payment processing system that supports multiple payment methods, such as credit cards,
bank transfers, and digital wallets. You want to add support for a new payment method without modifying the existing
codebase.

Solution with the Open/Closed Principle:

To apply the Open/Closed Principle, you can create an abstract PaymentProcessor class that defines a common interface for
all payment methods. Each payment method (e.g., CreditCardPaymentProcessor, BankTransferPaymentProcessor) implements this
interface with its specific behavior.

By using polymorphism and abstraction, you can add new payment methods by creating new classes that extend the
PaymentProcessor class without modifying the existing code. This allows you to extend the system's functionality without
changing its core implementation.

Benefits of the Open/Closed Principle:

1. Flexibility: The Open/Closed Principle allows you to add new features or behaviors to a software system without
modifying existing code, providing flexibility and extensibility.

2. Maintainability: By separating the core implementation from the extension points, the Open/Closed Principle helps
to create maintainable and modular software systems.

3. Reusability: The Open/Closed Principle promotes code reuse by allowing you to create new classes that extend the
behavior of existing classes without modifying them.

4. Scalability: The Open/Closed Principle supports the scalability of software systems by enabling you to add new
features or behaviors as the system grows.

By following the Open/Closed Principle, you can create software systems that are flexible, maintainable, and extensible,
making them easier to adapt to changing requirements and future enhancements.
"""

# Open/Closed Principle Example

from abc import ABC, abstractmethod


class BadPaymentService:
    @staticmethod
    def process_payment(amount, method):
        if method == "credit_card":
            print(f"Processing credit card payment of ${amount}")
        elif method == "bank_transfer":
            print(f"Processing bank transfer payment of ${amount}")
        elif method == "digital_wallet":
            print(f"Processing digital wallet payment of ${amount}")
        else:
            print("Unsupported payment method")


# Client code
bad_payment_service = BadPaymentService()
bad_payment_service.process_payment(100, "credit_card")
bad_payment_service.process_payment(200, "bank_transfer")
bad_payment_service.process_payment(50, "digital_wallet")
bad_payment_service.process_payment(75, "cryptocurrency")

# Output:
# Processing credit card payment of $100
# Processing bank transfer payment of $200
# Processing digital wallet payment of $50
# Unsupported payment method

"""
In this example, we have a BadPaymentService class that processes payments using different payment methods (credit card,
bank transfer, digital wallet). The process_payment method takes an amount and a payment method as arguments and
implements the payment processing logic using conditional statements.

The problem with this implementation is that it violates the Open/Closed Principle. If we want to add a new payment
method (e.g., cryptocurrency), we would need to modify the existing code by adding a new conditional branch. This
approach is not scalable and violates the principle of open for extension but closed for modification.

To apply the Open/Closed Principle, we can refactor the code by creating an abstract PaymentProcessor class that defines
a common interface for all payment methods. Each payment method (e.g., CreditCardPaymentProcessor, BankTransferPaymentProcessor)
will implement this interface with its specific behavior. The PaymentService class will use the PaymentProcessor interface
to process payments without knowing the specific payment method implementation.

Let's refactor the code to apply the Open/Closed Principle:
"""


# Abstract class for Payment Processor
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


# Concrete class for Credit Card Payment Processor
class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


# Concrete class for Bank Transfer Payment Processor
class BankTransferPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")


# Concrete class for Digital Wallet Payment Processor
class DigitalWalletPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing digital wallet payment of ${amount}")


# Client code
class PaymentService:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def process_payment(self, amount):
        self.payment_processor.process_payment(amount)


if __name__ == "__main__":
    # Create instances of payment processors
    credit_card_processor = CreditCardPaymentProcessor()
    bank_transfer_processor = BankTransferPaymentProcessor()
    digital_wallet_processor = DigitalWalletPaymentProcessor()

    # Create payment service instances with different payment processors
    credit_card_service = PaymentService(credit_card_processor)
    bank_transfer_service = PaymentService(bank_transfer_processor)
    digital_wallet_service = PaymentService(digital_wallet_processor)

    # Process payments using different payment methods
    credit_card_service.process_payment(100)
    bank_transfer_service.process_payment(200)
    digital_wallet_service.process_payment(50)

    # Add a new payment method without modifying existing code
    class CryptocurrencyPaymentProcessor(PaymentProcessor):
        def process_payment(self, amount):
            print(f"Processing cryptocurrency payment of ${amount}")


    cryptocurrency_processor = CryptocurrencyPaymentProcessor()
    cryptocurrency_service = PaymentService(cryptocurrency_processor)
    cryptocurrency_service.process_payment(75)

# Output:
# Processing credit card payment of $100
# Processing bank transfer payment of $200
# Processing digital wallet payment of $50
# Processing cryptocurrency payment of $75

"""
In this example, we have applied the Open/Closed Principle by creating an abstract PaymentProcessor class that defines
a common interface for all payment methods. We have implemented concrete payment processor classes 
(CreditCardPaymentProcessor, BankTransferPaymentProcessor, DigitalWalletPaymentProcessor) that extend the 
PaymentProcessor class and provide specific implementations for processing payments.

The PaymentService class uses the PaymentProcessor interface to process payments without knowing the specific payment
method implementation. This decouples the client code from the concrete payment processor classes, making it open for
extension (adding new payment methods) but closed for modification (existing code remains unchanged).

    When we add a new payment method (CryptocurrencyPaymentProcessor) by extending the PaymentProcessor class, we can
    create a new instance of PaymentService with the new payment processor without modifying the existing code. This
    demonstrates how the Open/Closed Principle allows us to add new features without changing the core implementation.
    
By following the Open/Closed Principle, you can create software systems that are flexible, maintainable, and extensible,
enabling you to adapt to changing requirements and add new features with ease.
"""
