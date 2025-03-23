# This program defines a function that calculates the sum of a list of numbers.

def sum_of_numbers(numbers):
    """
    This function takes a list of numbers and returns their sum.
    :param numbers: list of numerical values
    :return: sum of the numbers
    """
    return sum(numbers)  # Using built-in sum function to calculate total

# Example usage
numbers_list = [1, 2, 3, 4, 5]  # Defining a list of numbers
result = sum_of_numbers(numbers_list)  # Calling the function
print(f"The sum of the numbers {numbers_list} is {result}")  # Printing the result