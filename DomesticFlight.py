from Flight import Flight

class DomesticFlight(Flight):
    def get_flight_details(self):
        return f"Domestic Flight - Number: {self.flight_number}, Origin: {self.origin}, Destination: {self.destination}, Price: ${self.ticket_price}"
