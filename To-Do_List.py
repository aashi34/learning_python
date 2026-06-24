todo_list = []

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "Status": "Pending"})
    print("New task added successfully!")

def view_tasks():
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        print(f"Total Tasks: {len(todo_list)}")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task['task']} - {task['Status']}")
    print("\n")

def remove_task():
    if len(todo_list) == 0:
        print("No tasks to remove.")
    else:
        try:
            search_index = int(input("Enter the task number to remove: ")) - 1

            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task '{removed_task['task']}' removed successfully!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

def mark_completed():
    if len(todo_list) == 0:
        print("No tasks to mark as completed.")
    else:
        try:
            search_index = int(input("Enter the task number to mark as completed: ")) - 1

            if 0 <= search_index < len(todo_list):
                todo_list[search_index]["Status"] = "Completed"
                print(f"Task '{todo_list[search_index]['task']}' marked as completed!")
            else:
                print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")

def menu():
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            remove_task()

        elif choice == "4":
            mark_completed()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()