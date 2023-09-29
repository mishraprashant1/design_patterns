"""
The Chain of Responsibility Design Pattern is a behavioral pattern that allows you to pass requests along a chain of
handlers. Each handler decides whether to process the request or pass it to the next handler in the chain.
This pattern promotes loose coupling between sender and receiver of a request and can be useful in scenarios where
multiple objects can handle a request, and you want to determine the appropriate handler dynamically.

Let's explore this pattern with a real-life example:

Imagine you are developing a help desk ticketing system for an IT support team. Users can submit various types of
requests, such as hardware issues, software problems, and network-related queries. Depending on the type of request,
the system should route the ticket to the appropriate support team (e.g., hardware team, software team, network team)
for resolution.

Solution with the Chain of Responsibility Pattern:
"""

from abc import ABC, abstractmethod


# Abstract Handler
class SupportTeam(ABC):
    def __init__(self, name):
        self.name = name
        self.next_team = None

    def set_next_team(self, next_team):
        self.next_team = next_team

    @abstractmethod
    def handle_request(self, request):
        pass


# Concrete Handlers
class HardwareTeam(SupportTeam):
    def handle_request(self, request):
        if request.type == "Hardware":
            print(f"{self.name} team is handling a hardware issue.")
        elif self.next_team:
            self.next_team.handle_request(request)


class SoftwareTeam(SupportTeam):
    def handle_request(self, request):
        if request.type == "Software":
            print(f"{self.name} team is handling a software problem.")
        elif self.next_team:
            self.next_team.handle_request(request)


class NetworkTeam(SupportTeam):
    def handle_request(self, request):
        if request.type == "Network":
            print(f"{self.name} team is handling a network-related query.")
        elif self.next_team:
            self.next_team.handle_request(request)


# Request class
class Request:
    def __init__(self, req_type):
        self.type = req_type


# Client code
if __name__ == "__main__":
    # Create support teams
    hardware_team = HardwareTeam("Hardware")
    software_team = SoftwareTeam("Software")
    network_team = NetworkTeam("Network")

    # Set up the chain of responsibility
    hardware_team.set_next_team(software_team)
    software_team.set_next_team(network_team)

    # Create and process requests
    request1 = Request("Hardware")
    request2 = Request("Software")
    request3 = Request("Network")

    hardware_team.handle_request(request1)
    hardware_team.handle_request(request2)
    hardware_team.handle_request(request3)
