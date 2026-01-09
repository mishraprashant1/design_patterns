"""
The Observer pattern is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects
about any events that happen to the object they're observing. It establishes a one-to-many relationship between subjects
and observers, where multiple observers are notified for any state changes in the subject.

Imagine you're building a weather application that displays the current temperature, humidity, and pressure. You want to
notify multiple displays (e.g., current conditions, statistics, forecast) whenever the weather data changes. You also want
to ensure that new display elements can be added without modifying the weather data source.

Solution with the Observer Pattern:
"""

from abc import ABC, abstractmethod


# Subject (Observable)
class WeatherData:
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()


# Observer
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


# Concrete Observers
class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current Conditions: {temperature}F degrees and {humidity}% humidity")


class StatisticsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Statistics: {temperature}F degrees and {humidity}% humidity")


class ForecastDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Forecast: More sunny weather ahead!")


if __name__ == "__main__":
    weather_data = WeatherData()

    current_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()

    weather_data.register_observer(current_display)
    weather_data.register_observer(statistics_display)
    weather_data.register_observer(forecast_display)

    weather_data.set_measurements(80, 65, 30.4)
    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)

    weather_data.remove_observer(statistics_display)

    weather_data.set_measurements(79, 75, 29.2)

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
