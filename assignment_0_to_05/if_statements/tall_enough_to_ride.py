def tall_enough():
    """
    Continuously asks the user for their height and checks if they are tall enough
    to ride a rollercoaster. The program stops when the user enters nothing.
    """
    MIN_HEIGHT = 50  # Minimum height required to ride

    while True:
        height = input("How tall are you? ")  # Get user input

        if height == "":  # Stop the program if input is empty
            print("Exiting the program. Have a great day!")
            break

        try:
            height = int(height)  # Convert input to integer
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")  # Handle non-numeric input

# Run the function
tall_enough()

