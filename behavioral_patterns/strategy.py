"""
The Strategy pattern is a behavioral design pattern that enables selecting an algorithm at runtime — a strategy — from a family of algorithms.

Imagine you're building a navigation application that provides different routes to a destination based on the user's
preferences. You want to allow users to choose between different routing algorithms, such as the fastest route, the
shortest route, or the most scenic route. You also want to make it easy to add new routing algorithms in the future.

Solution with the Strategy Pattern:
"""

from abc import ABC, abstractmethod


# Context
class NavigationApp:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def build_route(self, source, destination):
        return self.strategy.build_route(source, destination)


# Strategy
class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, source, destination):
        pass


# Concrete Strategies
class FastestRouteStrategy(RouteStrategy):
    def build_route(self, source, destination):
        return f"Calculating the fastest route from {source} to {destination}..."


class ShortestRouteStrategy(RouteStrategy):
    def build_route(self, source, destination):
        return f"Calculating the shortest route from {source} to {destination}..."


class ScenicRouteStrategy(RouteStrategy):
    def build_route(self, source, destination):
        return f"Calculating the most scenic route from {source} to {destination}..."


# Usage
if __name__ == "__main__":
    app = NavigationApp(FastestRouteStrategy())
    print(app.build_route("New York", "Los Angeles"))

    app.set_strategy(ShortestRouteStrategy())
    print(app.build_route("San Francisco", "Seattle"))

    app.set_strategy(ScenicRouteStrategy())
    print(app.build_route("Chicago", "Miami"))


# One more example

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def notify(self, temperature, wind_speed, visibility):
        pass


class ATC(Observer):
    def notify(self, temperature, wind_speed, visibility):
        if visibility < 5 or wind_speed > 25:
            print("Bad weather for air crafts")
        else:
            print("Good weather for air crafts")


class ColdStorage(Observer):
    def notify(self, temperature, wind_speed, visibility):
        if temperature > 35:
            print("Turning on the wind blowers")
        else:
            print("Weather is pleasant for cold storage")


class HighwayManagement(Observer):
    def notify(self, temperature, wind_speed, visibility):
        if visibility < 2:
            print("Bad visibility for driving on highway")
        elif visibility < 5:
            print("Descent visibility for driving on highway")
        else:
            print("Very Good visibility for driving on highway")


class Subject:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def publish(self, temperature, wind_speed, visibility):
        for observer in self.observers:
            observer.notify(temperature, wind_speed, visibility)


if __name__ == "__main__":
    obj_1 = ATC()
    obj_2 = ColdStorage()
    obj_3 = HighwayManagement()

    observer_1 = Subject()
    observer_2 = Subject()

    observer_1.register(obj_1)
    observer_1.register(obj_2)

    observer_2.register(obj_3)

    observer_1.publish(temperature=40, wind_speed=25, visibility=5)
    observer_2.publish(temperature=50, wind_speed=50, visibility=1)
