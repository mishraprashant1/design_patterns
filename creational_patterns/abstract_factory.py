from abc import ABC, abstractmethod
from factory import TransportFactory


class Logistics(ABC):
    @abstractmethod
    def get_logistics(self):
        pass

    def plan_delivery(self, package):
        transport = self.get_logistics()
        transport.deliver(package)


class LandLogistics(Logistics):
    def get_logistics(self):
        print('Using Land Logistics')
        return TransportFactory.create_transport('truck')


class SeaLogistics(Logistics):
    def get_logistics(self):
        print('Using Sea Logistics')
        return TransportFactory.create_transport('ship')


class LogisticFactory:
    @staticmethod
    def create_logistics(logistics_type):
        if logistics_type == 'land':
            return LandLogistics()
        elif logistics_type == 'sea':
            return SeaLogistics()
        else:
            raise Exception('Invalid logistics type')


if __name__ == '__main__':
    LogisticFactory.create_logistics('land').plan_delivery('Laptops')
    LogisticFactory.create_logistics('sea').plan_delivery('Phones')
