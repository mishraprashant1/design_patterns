"""

📌 Low-Level Design Problem: Swiggy-like Food Delivery System

Design a food delivery platform similar to Swiggy that allows users to discover restaurants, place orders, and get food delivered.

Core Requirements

Users should be able to:

Register and log in

Browse restaurants based on location

View restaurant menus

Add items to cart and place orders

Restaurants should be able to:

Register on the platform

Add/update menu items

Accept or reject orders

Delivery partners should be able to:

Go online/offline

Accept delivery requests

Update delivery status

Order Flow

User places an order

System assigns a delivery partner

Order moves through states (PLACED → CONFIRMED → PREPARED → PICKED_UP → DELIVERED / CANCELLED)

Constraints / Considerations

Multiple users can place orders concurrently

One delivery partner can handle only one active order at a time

System should support order cancellation

Design should be extensible for:

Multiple payment methods

Ratings & reviews

Offers / coupons (optional)

Expectations

Focus on class design, relationships, and core workflows

You may assume in-memory storage unless stated otherwise

APIs / persistence / scalability are out of scope unless you choose to include them

"""
import random
from abc import ABC, abstractmethod


class Address:
    address_line_1: str
    address_line_2: str
    city: str
    state: str
    zip_code: str

    def __init__(self, address_line_1, address_line_2, city, state, zip_code):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state = state
        self.zip_code = zip_code


class User:
    name: str
    address: Address
    phone: str
    email: str

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email


class Food:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    name: str
    address: Address
    menu: list[Food]

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = []

    def add_food(self, food: Food):
        self.menu.append(food)

    def update_food(self, name: str, price: float):
        for food in self.menu:
            if food.name == name:
                food.price = price
                break

    def remove_food(self, name: str):
        for food in self.menu:
            if food.name == name:
                self.menu.remove(food)
                break

    def display_menu(self):
        menu = self.menu
        for food in menu:
            print(f"{food.name}: {food.price}")


class DeliveryRider:
    name: str
    is_available: bool

    def __init__(self, name, is_available=True):
        self.name = name
        self.is_available = is_available

    def set_availability(self, is_available: bool):
        self.is_available = is_available


class Item:
    food: Food
    quantity: float


class Cart:
    customer: User
    restaurant: Restaurant
    items = list[Item]

    def __init__(self, customer, restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    @property
    def cart_total(self):
        total = 0
        for item in self.items:
            total += item.quantity
        return total


users: list[User] = []
restaurants: list[Restaurant] = []
carts: list[Cart] = []
delivery_riders: list[DeliveryRider] = []


class OrderStatusEnum:
    PENDING = 'PENDING'
    PAYMENT_IN_PROGRESS = 'PAYMENT_IN_PROGRESS'
    PAYMENT_DONE = 'PAYMENT_DONE'
    QUEUED = 'QUEUED'
    IN_DELIVERY = 'IN_DELIVERY'
    DELIVERED = 'DELIVERED'


class Order:
    id: int
    cart: Cart
    is_order_accepted_by_restaurant: bool
    delivery_rider: DeliveryRider
    status = OrderStatusEnum.PENDING

    def __init__(self, cart):
        self.cart = cart

    def accept_or_reject_order(self, acceptance_status):
        self.is_order_accepted_by_restaurant = acceptance_status
        publish_status = PublishOrderStatus()
        publish_status.notify(self)


class Observer(ABC):
    @abstractmethod
    def notify(self, order: Order):
        pass


class Method(ABC):
    name: str


class CardPaymentMethod(Method):
    name = "Card Payment Method"


class UPIPaymentMethod(Method):
    name = "UPI Payment Method"


class Gateway:
    name: str

    def __init__(self, method: Method):
        self.method = method

    def pay(self, order: Order):
        order.status = OrderStatusEnum.PAYMENT_IN_PROGRESS
        print(f"Paying for Order id: {order.id}")
        print(f"Amount: {order.cart.cart_total}")
        print(f"Payment gateway: {self.name}")
        print(f"Method: {self.method.name}")
        order.status = OrderStatusEnum.PAYMENT_DONE


class RazorpayGateway(Gateway):
    name = "Razorpay Gateway"


class GooglePayGateway(Gateway):
    name = "Google Pay"


class Payment:
    @staticmethod
    def pay(order: Order, payment_method: str, gateway: str):
        if payment_method == "CARD":
            method = CardPaymentMethod()
        else:
            method = UPIPaymentMethod()

        if gateway == "Razorpay":
            gateway = RazorpayGateway(method)
        else:
            gateway = GooglePayGateway(method)

        gateway.pay(order)


class OrderFacade:
    def __init__(self, order: Order):
        self.order = order

    def process_order(self):
        self.order.status = OrderStatusEnum.PAYMENT_IN_PROGRESS
        payment_method = input("Payment method: ")
        gateway = input("Gateway: ")
        Payment.pay(self.order, payment_method, gateway)
        if self.order.status == OrderStatusEnum.PAYMENT_DONE:
            accept_or_reject = True if random.randint(1, 2) == 1 else False
            self.order.accept_or_reject_order(accept_or_reject)
            if accept_or_reject:
                self.order.status = OrderStatusEnum.QUEUED


class AssignRider(Observer):
    def notify(self, order: Order):
        if order.is_order_accepted_by_restaurant:
            for rider in delivery_riders:
                if rider.is_available:
                    order.delivery_rider = rider
        else:
            print("Order was rejected by restaurant, hence not assigning rider.")


class SendOrderStatusToUser(Observer):
    def notify(self, order: Order):
        user = order.cart.customer
        status = 'Accepted' if order.is_order_accepted_by_restaurant else 'Rejected'
        print(f"Sending notification to {user.name}: Order {status}")


class PublishToAnalytics(Observer):
    def notify(self, order: Order):
        print(f"Sending order details to analytics {order.cart.customer.name}: {order.cart.cart_total}")


class PublishOrderStatus(Observer):
    def notify(self, order: Order):
        assign_rider = AssignRider()
        send_order_status_to_user = SendOrderStatusToUser()
        publish_to_analytics = PublishToAnalytics()

        assign_rider.notify(order)
        send_order_status_to_user.notify(order)
        publish_to_analytics.notify(order)


def add_new_user():
    name = input("What is your name? ")
    phone = input("What is your phone number? ")
    email = input("What is your email address? ")
    address = Address(
        address_line_1=input("What is your address line 1? "),
        address_line_2=input("What is your address line 2? "),
        city=input("What is your city? "),
        state=input("What is your state? "),
        zip_code=input("What is your zip code? "),
    )

    user = User(
        name=name,
        address=address,
        phone=phone,
        email=email,
    )

    users.append(user)


def add_new_restaurant():
    name = input("What is your name? ")
    address = Address(
        address_line_1=input("What is your address line 1? "),
        address_line_2=input("What is your address line 2? "),
        city=input("What is your city? "),
        state=input("What is your state? "),
        zip_code=input("What is your zip code? "),
    )

    restaurant = Restaurant(
        name=name,
        address=address,
    )

    restaurants.append(restaurant)


def add_food_to_restaurant():
    name = input("To which restaurant do you want to add? ")
    restaurant = None
    for r in restaurants:
        if r.name == name:
            restaurant = r
            break

    food = Food(
        name=input("What is your food name? "),
        price=float(input("What is your food price? ")),
    )
    restaurant.add_food(food)


def check_menu():
    name = input("To which restaurant do you want to add? ")
    restaurant = None
    for r in restaurants:
        if r.name == name:
            restaurant = r
            break

    restaurant.display_menu()


if __name__ == '__main__':
    print("Welcome to Swiggy V2!")
    while True:
        print("What would you like to do?")
        print("1. Add user")
        print("2. Add restaurant")
        print("3. Add food to restaurant")
        print("4. Check menu")

        choice = input("What would you like to do? ")
        if choice == "1":
            add_new_user()
        elif choice == "2":
            add_new_restaurant()
        elif choice == "3":
            add_food_to_restaurant()
        elif choice == "4":
            check_menu()
        else:
            print("Invalid choice")
        print("-" * 30)
