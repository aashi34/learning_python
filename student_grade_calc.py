## Student Grade Calculator

print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter Student Name: ")
subjects = int(input("Enter Number of Subjects: "))

total_marks = 0

for i in range(subjects):
    while True:
        try:
            marks = float(input(f"Enter Marks for Subject {i + 1} (0-100): "))

            if 0 <= marks <= 100:
                total_marks += marks
                break
            else:
                print("Marks should be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

average_marks = total_marks / subjects

# Grade Calculation
if average_marks >= 90:
    grade = "A"
    remark = "Excellent"
elif average_marks >= 80:
    grade = "B"
    remark = "Very Good"
elif average_marks >= 70:
    grade = "C"
    remark = "Good"
elif average_marks >= 60:
    grade = "D"
    remark = "Needs Improvement"
else:
    grade = "F"
    remark = "Fail"

print("\n===== RESULT =====")
print(f"Student Name : {name}")
print(f"Subjects     : {subjects}")
print(f"Total Marks  : {total_marks:.2f}")
print(f"Average      : {average_marks:.2f}")
print(f"Grade        : {grade}")
print(f"Remark       : {remark}")
