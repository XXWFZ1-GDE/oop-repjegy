from typing import List

from Booking import Booking
from Airline import Airline

class BookingSystem:
    __curr_max_booking_id = 6

    def __init__(self, airlines: List[Airline], bookings: List[Booking]):
        self.airlines = airlines
        self.bookings = bookings

    def book_ticket(self, flight_number, passenger_name):
        for airline in self.airlines:
            for flight in airline.flights:
                if flight.flight_number == flight_number:
                    booking_id = self.__curr_max_booking_id + 1
                    self.__curr_max_booking_id = booking_id
                    booking = Booking(booking_id, flight, passenger_name)
                    self.bookings.append(booking)
                    print(f"Booking successful! Booking ID: {booking_id}")
                    return
            print("Flight not found. Please check the flight number.")

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                self.bookings.remove(booking)
                print(f"Booking ID {booking_id} has been canceled.")
                return
        print("Booking ID not found. Please try again.")

    def list_bookings(self):
        if not self.bookings:
            print("No current bookings.")
            return
        print("Current bookings:")
        for booking in self.bookings:
            print(booking.get_booking_details())