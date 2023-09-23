"""
The Facade Design Pattern is a structural pattern that provides a simplified interface to a complex system of classes,
libraries, or APIs. It hides the complexities of the underlying system and exposes a unified, high-level interface for
clients to interact with. Let's explore this pattern with a real-life example:

Real-Life Example Problem:
Imagine you are developing a modern home entertainment system that includes a TV, a sound system, a gaming console,
and smart lighting. Each of these components has its own complex set of operations and controls. Your users want a
simple and unified interface to control all these devices without needing to interact with each component individually.

Solution with the Facade Pattern:
The Facade Pattern suggests that you create a facade class that acts as a single entry point for clients to interact
with the complex system. The facade class encapsulates the functionality of the underlying components and provides a
simplified interface.
"""


# Complex subsystems
class TV:
    def turn_on(self):
        print("Turning on the TV")

    def turn_off(self):
        print("Turning off the TV")


class SoundSystem:
    def turn_on(self):
        print("Turning on the Sound System")

    def turn_off(self):
        print("Turning off the Sound System")


class GamingConsole:
    def start_game(self):
        print("Starting the game")

    def stop_game(self):
        print("Stopping the game")


class SmartLighting:
    def dim_lights(self):
        print("Dimming the lights")

    def brighten_lights(self):
        print("Brightening the lights")


# Facade class
class EntertainmentSystemFacade:
    def __init__(self):
        self.tv = TV()
        self.sound_system = SoundSystem()
        self.gaming_console = GamingConsole()
        self.smart_lighting = SmartLighting()

    def start_movie_mode(self):
        print("Starting Movie Mode")
        self.tv.turn_on()
        self.sound_system.turn_on()
        self.smart_lighting.dim_lights()

    def stop_movie_mode(self):
        print("Stopping Movie Mode")
        self.tv.turn_off()
        self.sound_system.turn_off()
        self.smart_lighting.brighten_lights()

    def start_gaming_mode(self):
        print("Starting Gaming Mode")
        self.gaming_console.start_game()
        self.sound_system.turn_on()
        self.smart_lighting.dim_lights()

    def stop_gaming_mode(self):
        print("Stopping Gaming Mode")
        self.gaming_console.stop_game()
        self.sound_system.turn_off()
        self.smart_lighting.brighten_lights()


# Client code
if __name__ == "__main__":
    entertainment_system = EntertainmentSystemFacade()

    print("User wants to watch a movie:")
    entertainment_system.start_movie_mode()
    # ... User enjoys the movie ...
    entertainment_system.stop_movie_mode()

    print("\nUser wants to play a game:")
    entertainment_system.start_gaming_mode()
    # ... User plays the game ...
    entertainment_system.stop_gaming_mode()
