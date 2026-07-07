## Create a Movie Ticket Booking System in Python Seat booking Available/Booked seats Movie selection Ticket confirmation
class MovieTicketBookingSystem:
    def __init__(self):
        self.movies = {
            "1": {"name": "Inception", "seats": 10},
            "2": {"name": "The Dark Knight", "seats": 8},
            "3": {"name": "Interstellar", "seats": 12}
        }
        self.booked_seats = {}

    def display_movies(self):
        print("Available Movies:")
        for key, movie in self.movies.items():
            print(f"{key}. {movie['name']} - Available Seats: {movie['seats']}")

    def book_ticket(self, movie_choice, seats_to_book):
        if movie_choice in self.movies:
            available_seats = self.movies[movie_choice]["seats"]
            if seats_to_book <= available_seats:
                self.movies[movie_choice]["seats"] -= seats_to_book
                self.booked_seats[movie_choice] = self.booked_seats.get(movie_choice, 0) + seats_to_book
                print(f"Successfully booked {seats_to_book} seat(s) for {self.movies[movie_choice]['name']}.")
            else:
                print(f"Only {available_seats} seat(s) available for {self.movies[movie_choice]['name']}.")
        else:
            print("Invalid movie choice.")

    def main(self):
        while True:
            self.display_movies()
            choice = input("Enter the movie number to book tickets (or 'exit' to quit): ")
            if choice.lower() == 'exit':
                break
            if choice in self.movies:
                try:
                    seats = int(input("Enter number of seats to book: "))
                    self.book_ticket(choice, seats)
                except ValueError:
                    print("Please enter a valid number of seats.")
            else:
                print("Invalid choice. Please select a valid movie number.")
    
if __name__ == "__main__":
    booking_system = MovieTicketBookingSystem()
    booking_system.main()
    