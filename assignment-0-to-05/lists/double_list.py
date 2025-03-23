# This program defines a function that doubles each element in a list of numbers.

def double_numbers(numbers):
    """
    This function takes a list of numbers and returns a new list with each number doubled.
    :param numbers: list of numerical values
    :return: list with doubled values
    """
    return [num * 2 for num in numbers]  # Using list comprehension to double each element

# Example usage
numbers_list = [1, 2, 3, 4]  # Defining a list of numbers
result = double_numbers(numbers_list)  # Calling the function
print(f"The doubled numbers are: {result}")  # Printing the result
