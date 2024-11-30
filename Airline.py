class Airline:
    def __init__(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def remove_flight(self, flight):
        self.flights.remove(flight)

    def list_flights(self):
        return [flight.get_flight_details() for flight in self.flights]
