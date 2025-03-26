def main():
    # Create a list called fruit_list that contains the following fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the original list
    print("Original list:", fruit_list)

    # Add 'mango' to the list
    fruit_list.append('mango')
    
    # Remove 'banana' from the list
    fruit_list.remove('banana')
    
    # Print the updated list
    print("Updated list:", fruit_list)

    # Print the first and last fruit in the list
    print("First fruit:", fruit_list[0])
    print("Last fruit:", fruit_list[-1])

if __name__ == "__main__":
    main()
