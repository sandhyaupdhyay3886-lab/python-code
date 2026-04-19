#Create a simple phone book using a dictionary where name is the key and phone number is the value.
#Features Students should implement: Add new contact Display all contacts Search contact by name Delete a contact
# Dictionary to store student data
# Dictionary to store contacts
phone_book = {}

# 1. Add new contact
def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print("Contact added successfully!\n")

# 2. Display all contacts
def display_contacts():
    if len(phone_book) == 0:
        print("No contacts found!\n")
    else:
        print("Phone Book:")
        for name in phone_book:
            print(name, ":", phone_book[name])
        print()

# 3. Search contact
def search_contact():
    name = input("Enter name to search: ")
    if name in phone_book:
        print("Phone number of", name, "=", phone_book[name], "\n")
    else:
        print("Contact not found!\n")

# 4. Delete contact
def delete_contact():
    name = input("Enter name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found!\n")

# Menu-driven program
while True:
    print("----- PHONE BOOK MENU -----")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Exiting Phone Book...")
        break
    else:
        print("Invalid choice! Try again.\n")