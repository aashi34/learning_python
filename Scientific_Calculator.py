## Scientific Calculator in Python

import math

class ScientificCalculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

    def power(self, a, b):
        return a ** b

    def square_root(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "Error! Negative number."

    def sine(self, angle):
        return math.sin(math.radians(angle))

    def cosine(self, angle):
        return math.cos(math.radians(angle))

    def tangent(self, angle):
        return math.tan(math.radians(angle))

    def logarithm(self, number):
        if number > 0:
            return math.log10(number)
        else:
            return "Error! Invalid number."

    def natural_log(self, number):
        if number > 0:
            return math.log(number)
        else:
            return "Error! Invalid number."


def main():

    calc = ScientificCalculator()

    while True:
        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Logarithm")
        print("11. Natural Log")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "12":
            print("Thank you for using the calculator!")
            break

        elif choice in ["1", "2", "3", "4", "5"]:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", calc.add(num1, num2))

            elif choice == "2":
                print("Result:", calc.subtract(num1, num2))

            elif choice == "3":
                print("Result:", calc.multiply(num1, num2))

            elif choice == "4":
                print("Result:", calc.divide(num1, num2))

            elif choice == "5":
                print("Result:", calc.power(num1, num2))

        elif choice in ["6", "7", "8", "9", "10", "11"]:

            number = float(input("Enter the number/angle: "))

            if choice == "6":
                print("Result:", calc.square_root(number))

            elif choice == "7":
                print("Result:", calc.sine(number))

            elif choice == "8":
                print("Result:", calc.cosine(number))

            elif choice == "9":
                print("Result:", calc.tangent(number))

            elif choice == "10":
                print("Result:", calc.logarithm(number))

            elif choice == "11":
                print("Result:", calc.natural_log(number))

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()