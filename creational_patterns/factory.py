from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self, package):
        pass


class Truck(Transport):
    def deliver(self, package):
        print(f"Truck delivering package: {package}")


class Ship(Transport):
    def deliver(self, package):
        print(f"Ship delivering package {package}")


class TransportFactory(ABC):
    @staticmethod
    def create_transport(transport_type):
        if transport_type == 'truck':
            return Truck()
        elif transport_type == 'ship':
            return Ship()
        else:
            raise Exception('Invalid transport type')


TransportFactory.create_transport('truck').deliver('Laptops')
TransportFactory.create_transport('ship').deliver('Phones')
