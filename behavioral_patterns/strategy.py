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
