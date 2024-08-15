from abc import ABC, abstractmethod
from collections import defaultdict


class Address:
    line_1: str = None
    line_2: str = None
    city: str = None
    state: str = None
    country: str = None
    pin_code: str = None
    lat: int = None
    long: int = None

    def __str__(self):
        return f'{self.line_1}, {self.line_2}, {self.city}, {self.state}, {self.country}, {self.pin_code}'


class AddressOfEnum:
    HOME = 'HOME'
    OFFICE = 'OFFICE'
    OTHER = 'OTHER'


class User:
    name: str = None
    id: int = None

    def __init__(self, user_id: int, name: str):
        self.name = name
        self.id = user_id

    def __hash__(self):
        return hash(self.id)


class Customer(User):
    address: dict[AddressOfEnum, Address] = {}

    def add_address(self, address_type: AddressOfEnum, address: Address):
        self.address[address_type] = address


class FoodItem:
    id: int = None
    name: str = None
    price: int = 0

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __hash__(self):
        return hash(self.id)


class Menu:
    items: dict[int, FoodItem] = {}

    def add(self, food_item: FoodItem):
        self.items[food_item.id] = food_item

    def remove(self, food_item: FoodItem):
        self.items.pop(food_item.id)

    def get_menu(self) -> dict[int, FoodItem]:
        return self.items


class Restaurant:
    id: int = None
    name: str = None
    address: Address = None
    menu: Menu = None

    def __init__(self, rest_id: int, name: str, address: Address):
        self.id = rest_id
        self.name = name
        self.address = address

    def add_in_menu(self, food_item: FoodItem):
        self.menu.add(food_item)

    def remove_from_menu(self, food_item: FoodItem):
        self.menu.remove(food_item)

    def display_menu(self):
        menu_items = self.menu.get_menu()
        for i, item in menu_items.items():
            print(f'{item.id}: {item.name} ------- {item.price}')


class BaseCart:
    __carts__: dict[Customer, dict] = defaultdict(dict)

    def __new__(cls, *args, **kwargs):
        customer: Customer = kwargs.get('user')
        if not customer:
            for arg in args:
                if isinstance(arg, Customer):
                    customer = arg
                    break

        restaurant: Restaurant = kwargs.get('restaurant')
        if not restaurant:
            for arg in args:
                if isinstance(arg, Restaurant):
                    restaurant = arg
                    break
        if customer not in cls.__carts__ or restaurant not in cls.__carts__[customer]:
            cls.__carts__[customer][restaurant] = super().__new__(cls)
        return cls.__carts__[customer][restaurant]


class Cart(BaseCart):
    user: Customer = None
    restaurant: Restaurant = None
    items: dict[FoodItem, int] = {}

    def __init__(self, user: Customer, restaurant: Restaurant):
        self.user = user
        self.restaurant = restaurant

    def add_to_cart(self, food_item: FoodItem, quantity: int):
        self.items[food_item] = quantity


class PaymentModeEnum:
    CASH = 'CASH'
    CARD = 'CARD'


class OrderStatusEnum:
    PENDING = 'PENDING'
    PAYMENT_IN_PROGRESS = 'PAYMENT_IN_PROGRESS'
    PAYMENT_DONE = 'PAYMENT_DONE'
    QUEUED = 'QUEUED'
    IN_DELIVERY = 'IN_DELIVERY'
    DELIVERED = 'DELIVERED'


class Payments(ABC):
    mode: PaymentModeEnum = None

    @abstractmethod
    def initiate_payment(self, amount):
        pass


class CashPayment(Payments):
    mode = PaymentModeEnum.CASH

    def initiate_payment(self, amount):
        print(f'Paying ${amount} via Cash')
        return True


class CreditCardPayment(Payments):
    mode = PaymentModeEnum.CARD

    def initiate_payment(self, amount):
        print(f'Paying ${amount} via Credit Card')
        return True


class PaymentFactory:
    @staticmethod
    def get_payment_mode(pay_by: str) -> Payments:
        if pay_by.lower() == 'cash':
            return CashPayment()
        elif pay_by.lower() == 'credit_card':
            return CreditCardPayment()
        raise Exception('Invalid payment mode given!')


class Order:
    id: int = None
    cart: Cart = None
    payment_mode: str = None
    is_payment_successful: bool = False
    status: OrderStatusEnum = None

    def get_discount(self) -> int:
        return 0

    def get_total_bill(self):
        items = self.cart.items
        total_amount = 0
        for item in items:
            total_amount += item.price
        total_amount -= (total_amount * self.get_discount())
        return total_amount


class DeliveryRider(User):
    curr_lat: int = None
    curr_long: int = None
    range_in_km: int = None
    is_on_duty: bool = False
    is_occupied: bool = False
    serves_to_pin_codes: list[int] = []

    def deliver_order(self, order):
        restaurant = order.cart.restaurant
        customer = order.cart.customer
        print(
            f'Delivery Rider: {self.name} is delivering order no. {order.id} from {str(restaurant.name)} to {str(customer.address)}')


class RiderOrchestrator:
    pin_code_to_rider_map: dict[int, DeliveryRider] = {}

    def get_closest_rider_from_restaurant(self, restaurant: Restaurant) -> DeliveryRider:
        pass


class Swiggy:
    restaurants: dict[int, Restaurant] = {}
    order_queue: list[Order]

    def add_restaurant(self, restaurant: Restaurant):
        self.restaurants[restaurant.id] = restaurant

    def place_order(self, order: Order):
        total_bill_amount = order.get_total_bill()
        payment_mode = PaymentFactory.get_payment_mode(order.payment_mode)
        order.is_payment_successful = payment_mode.initiate_payment(total_bill_amount)
        rider_orchestrator = RiderOrchestrator()
        delivery_rider = rider_orchestrator.get_closest_rider_from_restaurant(order.cart.restaurant)
