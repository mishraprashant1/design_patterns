"""
The Command Design Pattern is a behavioral pattern that encapsulates a request as an object, thereby allowing you to
parameterize clients with queues, requests, and operations. It also enables you to support undoable operations.
This pattern separates the sender of a request from its receiver, allowing for decoupling and flexibility in the
handling of requests.

Real-Life Example Problem:

Imagine you are building a remote control for a smart home. The remote control should allow users to perform various
actions on different smart devices like turning on lights, adjusting the thermostat, and locking the front door.
However, the remote control should also support undoing the last action.
"""

from abc import ABC, abstractmethod


# Receiver: Represents a smart device (e.g., light, thermostat, door)
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.state = "OFF"

    def turn_on(self):
        self.state = "ON"
        print(f"{self.name} is now ON")

    def turn_off(self):
        self.state = "OFF"
        print(f"{self.name} is now OFF")


# Command: Abstract command class
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Commands
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

    def undo(self):
        self.device.turn_off()


class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

    def undo(self):
        self.device.turn_on()


# Invoker: Remote control
class RemoteControl:
    def __init__(self):
        self.command_history = []

    def press_button(self, command):
        command.execute()
        self.command_history.append(command)

    def undo_last_command(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()


if __name__ == "__main__":
    # Create smart devices
    light = SmartDevice("Living Room Light")
    thermostat = SmartDevice("Thermostat")
    door = SmartDevice("Front Door")

    # Create commands
    turn_on_light = TurnOnCommand(light)
    turn_on_thermostat = TurnOnCommand(thermostat)
    turn_off_thermostat = TurnOffCommand(thermostat)
    turn_on_door = TurnOnCommand(door)

    # Create remote control
    remote = RemoteControl()

    # Press buttons on the remote control
    remote.press_button(turn_on_light)
    remote.press_button(turn_on_thermostat)
    remote.press_button(turn_off_thermostat)
    remote.press_button(turn_on_door)

    # Undo the last command
    remote.undo_last_command()
