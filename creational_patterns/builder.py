from abc import ABC, abstractmethod
from abstract_factory import LogisticFactory


class CheckoutBuilder(ABC):
    def __init__(self):
        self.cart = []
        self.cart_value = []
        self.cart_count = 0
        self.discount = 0
        self.delivery_date = None
        self.shipping_details = None

    @abstractmethod
    def get_cart_products(self):
        pass

    @abstractmethod
    def get_cart_total(self):
        pass

    @abstractmethod
    def get_cart_count(self):
        pass

    @abstractmethod
    def apply_discount(self):
        pass

    @abstractmethod
    def get_delivery_date(self):
        pass

    @abstractmethod
    def get_shipping_details(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class DefaultUserCheckoutBuilder(CheckoutBuilder):
    def get_cart_products(self):
        print("Getting cart products for default user")
        self.cart = [['Laptops', 1000], ['Mobiles', 2000], ['Tablets', 3000]]

    def get_cart_total(self):
        print("Getting cart total for default user")
        self.cart_value = sum([i[1] for i in self.cart])

    def get_cart_count(self):
        print("Getting cart count for default user")
        self.cart_count = len(self.cart)

    def apply_discount(self):
        print("Applying discount for default user")
        self.discount = 0
        self.cart_value = self.cart_value - self.discount

    def get_delivery_date(self):
        print("Getting delivery date for default user")
        self.delivery_date = '10th May 2021'

    def get_shipping_details(self):
        print("Getting shipping details for default user")
        self.shipping_details = 'Address of the user'

    def deliver(self):
        print("Delivering the products to the user")
        print('Here are the details:')
        print(f'Products: {self.cart}')
        print(f'Total: {self.cart_value}')
        print(f'Discount: {self.discount}')
        print(f'Delivery Date: {self.delivery_date}')
        print(f'Shipping Details: {self.shipping_details}')
        print('Thanks for shopping with us!')
        LogisticFactory.create_logistics('land').plan_delivery('Laptops')


class PrimeUserCheckoutBuilder(DefaultUserCheckoutBuilder):

    def apply_discount(self):
        print("Applying discount for prime user")
        self.discount = self.cart_value * 0.1
        self.cart_value = self.cart_value - self.discount

    def get_delivery_date(self):
        print("Getting delivery date for prime user")
        self.delivery_date = '5th May 2021'


class CheckoutDirector:
    def __init__(self, builder: CheckoutBuilder):
        self.builder = builder

    def construct(self):
        self.builder.get_cart_products()
        self.builder.get_cart_total()
        self.builder.get_cart_count()
        self.builder.apply_discount()
        self.builder.get_delivery_date()
        self.builder.get_shipping_details()
        self.builder.deliver()
        print('--------------------------------------------------------------')


if __name__ == '__main__':
    director = CheckoutDirector(DefaultUserCheckoutBuilder())
    director.construct()
    director = CheckoutDirector(PrimeUserCheckoutBuilder())
    director.construct()
