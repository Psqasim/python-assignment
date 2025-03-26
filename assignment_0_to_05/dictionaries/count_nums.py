# This program counts the occurrences of each number entered by the user.

# Create an empty dictionary to store number counts
number_counts: dict[int, int] = {}

# Continuously ask the user to enter numbers
while True:
    number = input("Enter a number (or press Enter to finish): ")
    
    # If the user presses Enter without typing a number, exit the loop
    if number == "":
        break
    
    # Convert input to an integer
    num = int(number)
    
    # Update the dictionary: increase count if number exists, otherwise set to 1
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

# Display the counts of each number
for num, count in number_counts.items():
    print(f"{num} appears {count} times.")

