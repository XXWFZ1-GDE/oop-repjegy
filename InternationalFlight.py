from Flight import Flight

class InternationalFlight(Flight):
    def get_flight_details(self):
        return f"International Flight - Number: {self.flight_number}, Origin: {self.origin}, Destination: {self.destination}, Price: ${self.ticket_price}"
