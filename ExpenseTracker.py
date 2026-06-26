expenses = []

def add_expense():
    try:
        amount = float(input("Enter the expense amount: "))
        description = input("Enter the expense description: ")
        expenses.append({"amount": amount, "description": description})
        print("Expense added successfully!")
    except ValueError:
        print("Please enter a valid amount.")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses to display.")
    else:
        print(f"Total Expenses: {len(expenses)}")
        for index, expense in enumerate(expenses, 1):
            print(f"{index}. {expense['description']}: ${expense['amount']:.2f}")

def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
    else:
        try:
            search_index = int(input("Enter the expense number to delete: ")) - 1

            if 0 <= search_index < len(expenses):
                deleted_expense = expenses.pop(search_index)
                print(f"Expense '{deleted_expense['description']}' deleted successfully!")
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

def menu():
    while True:
        print("\n===== EXPENSE TRACKER MENU =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Start the program
menu()