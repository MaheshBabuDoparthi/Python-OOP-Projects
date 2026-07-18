# Project 14: Hotel Room Booking System

class Hotel:

    def __init__(self, customer_name, room_number, room_type):
        self.customer_name = customer_name
        self.room_number = room_number
        self.room_type = room_type

    def show_details(self):
        print("Customer Name:", self.customer_name)
        print("Room Number:", self.room_number)
        print("Room Type:", self.room_type)

    def book_room(self):
        print("Room Booked Successfully!")

    def update_room(self, room_type):
        self.room_type = room_type
        print("Room Updated Successfully!")
        print("Updated Room:", self.room_type)

    def cancel_booking(self):
        print("Booking Cancelled Successfully!")

    def check_availability(self):
        print("Room Available")


bookings = []

while True:

    print("\n========== Hotel Room Booking System ==========")
    print("1. Book Room")
    print("2. View Booking")
    print("3. Update Room")
    print("4. Check Availability")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        customer_name = input("Enter Customer Name: ")
        room_number = int(input("Enter Room Number: "))
        room_type = input("Enter Room Type (AC/Non-AC): ")

        booking = Hotel(customer_name, room_number, room_type)
        bookings.append(booking)
        booking.book_room()

    elif choice == 2:

        if len(bookings) == 0:
            print("No Bookings Found!")
        else:
            for booking in bookings:
                booking.show_details()
                print("---------------------------")

    elif choice == 3:

        room = int(input("Enter Room Number: "))

        for booking in bookings:
            if booking.room_number == room:
                room_type = input("Enter New Room Type: ")
                booking.update_room(room_type)
                break
        else:
            print("Room Not Found!")

    elif choice == 4:

        room = int(input("Enter Room Number: "))

        for booking in bookings:
            if booking.room_number == room:
                booking.check_availability()
                break
        else:
            print("Room Not Available!")

    elif choice == 5:

        room = int(input("Enter Room Number: "))

        for booking in bookings:
            if booking.room_number == room:
                booking.cancel_booking()
                bookings.remove(booking)
                break
        else:
            print("Booking Not Found!")

    elif choice == 6:
        print("Thank You for Using Hotel Room Booking System!")
        break

    else:
        print("Invalid Choice!")