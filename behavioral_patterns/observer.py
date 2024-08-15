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
