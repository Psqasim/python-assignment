def access_element(lst, index):
    """Returns the element at the specified index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "Error: Index out of range."

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with a new value or returns an error message."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    return "Error: Index out of range."

def slice_list(lst, start, end):
    """Returns a sliced list based on start and end indices while handling out-of-range cases."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return f"Sliced list: {lst[start:end]}"
    return "Error: Invalid range."

def main():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]

    while True:
        print("\nOptions:\n1. Access an element\n2. Modify an element\n3. Slice the list\n4. See the List\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            index = int(input("Enter the index to access: "))
            print(access_element(my_list, index))

        elif choice == "2":
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == "3":
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print(slice_list(my_list, start, end))

        elif choice == "4":
            print(my_list)

        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
