contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts to display.")
    else:
        print(f"Total Contacts: {len(contacts)}")
        for index, contact in enumerate(contacts, 1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def delete_contact():
    if len(contacts) == 0:
        print("No contacts to delete.")
    else:
        try:
            search_index = int(input("Enter the contact number to delete: ")) - 1

            if 0 <= search_index < len(contacts):
                deleted_contact = contacts.pop(search_index)
                print(f"Contact '{deleted_contact['name']}' deleted successfully!")
            else:
                print("Invalid contact number.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

