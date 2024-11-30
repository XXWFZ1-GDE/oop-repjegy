from Airline import Airline
from Booking import Booking
from BookingSystem import BookingSystem
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight

# init
airlines = [Airline('Airline #1')]

airlines[0].add_flight(DomesticFlight(101, "Debrecen", "Budapest", 50))
airlines[0].add_flight(DomesticFlight(102, "Budapest", "Sopron", 75))
airlines[0].add_flight(InternationalFlight(201, "Budapest", "Zurich", 300))
airlines[0].add_flight(InternationalFlight(202, "Budapest", "London", 250))


bookings = [Booking(1, airlines[0].flights[0], "Alice"),
            Booking(2, airlines[0].flights[0], "Alice"),
            Booking(3, airlines[0].flights[2], "Bob"),
            Booking(4, airlines[0].flights[2], "Bob"),
            Booking(5, airlines[0].flights[1], "Charlie"),
            Booking(6, airlines[0].flights[1], "Bob")]

booking_system = BookingSystem(airlines, bookings)


# menu
while True:
    print("\n--- Flight Booking System ---")
    print("1. View available flights")
    print("2. Book a ticket")
    print("3. Cancel a booking")
    print("4. View current bookings")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable flights:")
        for flights in airlines[0].list_flights():
            print(flights)
    elif choice == "2":
        flight_number = input("Enter flight number: ")
        passenger_name = input("Enter passenger name: ")
        booking_system.book_ticket(flight_number, passenger_name)
    elif choice == "3":
        booking_id = int(input("Enter booking ID to cancel: "))
        booking_system.cancel_booking(booking_id)
    elif choice == "4":
        booking_system.list_bookings()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")