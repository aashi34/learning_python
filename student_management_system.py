## creating a student management system in python
students = []

def add_student(name, age, grade):
    students.append({"name": name, "age": age, "grade": grade})
    print(f"Student '{name}' added successfully!")

def view_students():
    if len(students) == 0:
        print("No students to display.")
    else:
        print(f"Total Students: {len(students)}")
        for index, student in enumerate(students, 1):
            print(f"{index}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def delete_student():
    if len(students) == 0:
        print("No students to delete.")
    else:
        try:
            search_index = int(input("Enter the student number to delete: ")) - 1

            if 0 <= search_index < len(students):
                deleted_student = students.pop(search_index)
                print(f"Student '{deleted_student['name']}' deleted successfully!")
            else:
                print("Invalid student number.")

        except ValueError:
            print("Please enter a valid number.")
    
if __name__ == "__main__":
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM MENU =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            add_student(name, age, grade)
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")