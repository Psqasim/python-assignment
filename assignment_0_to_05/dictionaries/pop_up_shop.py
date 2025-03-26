# This program calculates the total cost of fruits based on user input.

# Dictionary containing fruit names as keys and their prices per unit as values
fruit_prices: dict[str, float] = {
    "apple": 5.0,
    "durian": 15.0,
    "jackfruit": 12.5,
    "kiwi": 7.5,
    "rambutan": 8.0,
    "mango": 10.0
}

# Initialize total cost to 0
total_cost: float = 0.0

# Loop through each fruit in the dictionary
for fruit, price in fruit_prices.items():
    while True:
        try:
            # Ask user how many of each fruit they want
            quantity = int(input(f"How many ({fruit}) do you want?: "))
            
            # Ensure the quantity is not negative
            if quantity < 0:
                print("Please enter a valid non-negative number.")
                continue
            
            # Calculate cost for this fruit and add it to total cost
            total_cost += quantity * price
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Print the total cost formatted to 2 decimal places
print(f"\nYour total is ${total_cost:.2f}")
