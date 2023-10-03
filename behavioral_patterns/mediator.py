"""
The Mediator Design Pattern is a behavioral pattern that promotes loose coupling between objects by centralizing their
communication through a mediator object. It's used to manage and reduce dependencies between multiple objects, making
them interact through a mediator rather than directly with each other. This pattern is particularly useful when you have
a complex web of interactions between objects.

Imagine you're working on a smart home automation system. Your system consists of various smart devices like lights,
thermostats, and security cameras. These devices need to interact with each other based on certain conditions.
For instance, when a motion sensor detects movement, it should trigger the lights to turn on, and the thermostat should
adjust the temperature. You want to design a system that enables these interactions while keeping the devices decoupled
and easy to maintain.

Solution with the Mediator Pattern:
Mediator: This is the central component that coordinates interactions between smart devices. It knows about all the
devices and their capabilities.

Colleague (Smart Device): Colleagues are the individual smart devices in the system. Each device can send and receive
messages through the mediator.
"""

from abc import ABC, abstractmethod


# Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


# Colleague Interface
class SmartDevice(ABC):
    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    @abstractmethod
    def send_message(self, event):
        pass

    @abstractmethod
    def receive_message(self, event):
        pass


# Concrete Mediator
class HomeAutomationMediator(Mediator):
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def notify(self, sender, event):
        for device in self.devices:
            if device != sender:
                device.receive_message(event)


# Concrete Colleague: Light
class Light(SmartDevice):
    def send_message(self, event):
        print(f"{self.name} sends: {event}")
        self.mediator.notify(self, event)

    def receive_message(self, event):
        print(f"{self.name} receives: {event}")
        # Perform actions based on the event (e.g., turn on/off)


# Concrete Colleague: Thermostat
class Thermostat(SmartDevice):
    def send_message(self, event):
        print(f"{self.name} sends: {event}")
        self.mediator.notify(self, event)

    def receive_message(self, event):
        print(f"{self.name} receives: {event}")
        # Adjust temperature based on the event


# Concrete Colleague: Motion Sensor
class MotionSensor(SmartDevice):
    def send_message(self, event):
        print(f"{self.name} sends: {event}")
        self.mediator.notify(self, event)

    def receive_message(self, event):
        print(f"{self.name} receives: {event}")
        # Detect motion and trigger events (e.g., turn on lights)


# Client code
if __name__ == "__main__":
    # Create a home automation mediator
    mediator = HomeAutomationMediator()

    # Create smart devices
    light = Light(mediator, "Living Room Light")
    thermostat = Thermostat(mediator, "Living Room Thermostat")
    motion_sensor = MotionSensor(mediator, "Living Room Motion Sensor")

    # Add devices to the mediator
    mediator.add_device(light)
    mediator.add_device(thermostat)
    mediator.add_device(motion_sensor)

    # Simulate motion detection
    motion_sensor.send_message("Motion detected in the living room")
