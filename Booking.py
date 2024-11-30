from Airline import Airline

class Booking:
    def __init__(self, booking_id, flight, passenger_name):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger_name = passenger_name

    def get_booking_details(self):
        return f"Booking ID: {self.booking_id}, Passenger: {self.passenger_name}, Flight: {self.flight.get_flight_details()}"