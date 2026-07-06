## Create an Employee Management System in Python
class Employee:
    def __init__(self, employee_id, name, position, salary, date_of_joining):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.date_of_joining = date_of_joining


    def display_employee(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: ${self.salary}, Date of Joining: {self.date_of_joining}")
    
def main():
    employees = {}

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM MENU =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            employee_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = float(input("Enter employee salary: "))
            date_of_joining = input("Enter date of joining: ")
            employees[employee_id] = Employee(employee_id, name, position, salary, date_of_joining)
            print(f"Employee '{name}' added successfully!")

        elif choice == "2":
            if len(employees) == 0:
                print("No employees to display.")
            else:
                for emp in employees.values():
                    emp.display_employee()

        elif choice == "3":
            employee_id = input("Enter employee ID to update: ")
            if employee_id in employees:
                name = input("Enter new name (leave blank to keep current): ")
                position = input("Enter new position (leave blank to keep current): ")
                salary_input = input("Enter new salary (leave blank to keep current): ")
                date_of_joining = input("Enter new date of joining (leave blank to keep current): ")

                if name:
                    employees[employee_id].name = name
                if position:
                    employees[employee_id].position = position
                if salary_input:
                    employees[employee_id].salary = float(salary_input)
                if date_of_joining:
                    employees[employee_id].date_of_joining = date_of_joining

                print(f"Employee '{employee_id}' updated successfully!")
            else:
                print("Employee not found.")

        elif choice == "4":
            employee_id = input("Enter employee ID to delete: ")
            if employee_id in employees:
                del employees[employee_id]
                print(f"Employee '{employee_id}' deleted successfully!")
            else:
                print("Employee not found.")

        elif choice == "5":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
    