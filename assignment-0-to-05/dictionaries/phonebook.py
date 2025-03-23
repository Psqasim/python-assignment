# This program demonstrates using a dictionary to store and manage a phonebook.

# Create an empty dictionary to store contact names and phone numbers
phonebook: dict[str, str] = {}

def add_contact(name: str, number: str):
    """Adds a contact to the phonebook."""
    phonebook[name] = number
    print(f"Contact {name} added.")

def remove_contact(name: str):
    """Removes a contact from the phonebook if it exists."""
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} removed.")
    else:
        print(f"Contact {name} not found.")

def search_contact(name: str):
    """Searches for a contact and displays the phone number if found."""
    if name in phonebook:
        print(f"{name}'s number: {phonebook[name]}")
    else:
        print(f"Contact {name} not found.")

# Main program loop to interact with the phonebook
while True:
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")
    
    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        add_contact(name, number)
    
    elif choice == "2":
        name = input("Enter contact name to remove: ")
        remove_contact(name)
    
    elif choice == "3":
        name = input("Enter contact name to search: ")
        search_contact(name)
    
    elif choice == "4":
        print("\nPhonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    
    elif choice == "5":
        print("Exiting phonebook.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
