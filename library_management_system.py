## Creating a simple library management system in Python
class Library:
    def __init__(self, book_name, author, status ="Available"):
        self.book_name = book_name
        self.author = author
        self.status = status
    
    def add_book(self):
        print(f"Book '{self.book_name}' by {self.author} added to the library.")

    def view_book(self):
        print(f"Book Name: {self.book_name}, Author: {self.author}, status: {self.status}")

    def update_book(self, new_update):
        self.status = new_update
        print(f"Book '{self.book_name}' status updated to '{self.status}'.")

    def delete_book(self):
        print(f"Book '{self.book_name}' by {self.author} removed from the library.")

    def main():
        library_books = []

        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM MENU =====")
            print("1. Add Book")
            print("2. View Books")
            print("3. Update Book Status")
            print("4. Delete Book")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                book_name = input("Enter book name: ")
                author = input("Enter author name: ")
                new_book = Library(book_name, author)
                library_books.append(new_book)
                new_book.add_book()

            elif choice == "2":
                if len(library_books) == 0:
                    print("No books in the library.")
                else:
                    for index, book in enumerate(library_books, 1):
                        print(f"{index}. ", end="")
                        book.view_book()

            elif choice == "3":
                if len(library_books) == 0:
                    print("No books to update.")
                else:
                    try:
                        search_index = int(input("Enter the book number to update: ")) - 1
                        if 0 <= search_index < len(library_books):
                            new_status = input("Enter new status (Available/Checked Out): ")
                            library_books[search_index].update_book(new_status)
                        else:
                            print("Invalid book number.")
                    except ValueError:
                        print("Please enter a valid number.")

            elif choice == "4":
                if len(library_books) == 0:
                    print("No books to delete.")
                else:
                    try:
                        search_index = int(input("Enter the book number to delete: ")) - 1
                        if 0 <= search_index < len(library_books):
                            library_books[search_index].delete_book()
                            del library_books[search_index]
                        else:
                            print("Invalid book number.")
                    except ValueError:
                        print("Please enter a valid number.")

            elif choice == "5":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
if __name__ == "__main__":
    Library.main()