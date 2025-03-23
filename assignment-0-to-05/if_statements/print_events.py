def print_even_numbers(n: int) -> None:
    """
    Prints the first 'n' even numbers.
    """
    for i in range(n):
        print(i * 2, end=" ")  # Multiply by 2 to get even numbers

# Call the function to print the first 20 even numbers
print_even_numbers(20)
