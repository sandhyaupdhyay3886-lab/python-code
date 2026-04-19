#Create Attendance System where Faculty should: Add attendance for 5 students Count total present students
#Display absent students
# Dictionary to store attendance
attendance = {}

# 1. Add attendance for 5 students
def add_attendance():
    for i in range(5):
        name = input(f"Enter name of student {i+1}: ")
        status = input("Enter attendance (P for Present / A for Absent): ").upper()
        attendance[name] = status
    print("Attendance added successfully!\n")

# 2. Count total present students
def count_present():
    count = 0
    for status in attendance.values():
        if status == 'P':
            count += 1
    print("Total Present Students:", count, "\n")

# 3. Display absent students
def display_absent():
    print("Absent Students:")
    found = False
    for name, status in attendance.items():
        if status == 'A':
            print(name)
            found = True
    if not found:
        print("No absent students")
    print()

# Main program
add_attendance()
count_present()
display_absent()