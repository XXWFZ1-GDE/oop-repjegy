from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number, origin, destination, ticket_price):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.ticket_price = ticket_price

    @abstractmethod
    def get_flight_details(self):
        pass