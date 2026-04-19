#Create a program to manage student marks using dictionary.Features Store student name and marks
#Display all students Search student Find topper Calculate class average
# Dictionary to store student data
students = {}

# Function to add student
def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!\n")

# Function to display all students
def display_students():
    if not students:
        print("No records found!\n")
    else:
        print("\nStudent List:")
        for name, marks in students.items():
            print(f"{name} : {marks}")
        print()

# Function to search student
def search_student():
    name = input("Enter student name to search: ")
    if name in students:
        print(f"{name} has {students[name]} marks\n")
    else:
        print("Student not found!\n")

# Function to find topper
def find_topper():
    if not students:
        print("No records found!\n")
    else:
        topper = max(students, key=students.get)
        print(f"Topper is {topper} with {students[topper]} marks\n")

# Function to calculate average
def class_average():
    if not students:
        print("No records found!\n")
    else:
        avg = sum(students.values()) / len(students)
        print(f"Class Average = {avg:.2f}\n")

# Menu-driven program
while True:
    print("----- Student Marks Management -----")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Find Topper")
    print("5. Class Average")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        find_topper()
    elif choice == '5':
        class_average()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")