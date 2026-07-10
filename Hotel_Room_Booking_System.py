## Create a Hotel Room Booking System in Python
class HotelRoomBookingSystem:
    def __init__(self):
        self.rooms = {
            "101": {"type": "Single", "status": "Available"},
            "102": {"type": "Double", "status": "Available"},
            "103": {"type": "Suite", "status": "Available"}
        }
    
    def display_rooms(self):
        print("Available Rooms:")
        for room_number, details in self.rooms.items():
            print(f"Room {room_number}: Type: {details['type']}, Status: {details['status']}")
    
    def book_room(self, room_number):
        if room_number in self.rooms:
            if self.rooms[room_number]["status"] == "Available":
                self.rooms[room_number]["status"] = "Booked"
                print(f"Room {room_number} has been successfully booked.")
            else:
                print(f"Room {room_number} is already booked.")
        else:
            print(f"Room {room_number} does not exist.")

    def main(self):
        while True:
            self.display_rooms()
            choice = input("Enter the room number to book (or 'exit' to quit): ")
            if choice.lower() == 'exit':
                break
            self.book_room(choice)
    
if __name__ == "__main__":
    booking_system = HotelRoomBookingSystem()
    booking_system.main()