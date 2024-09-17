def sum_of_array(arr):
    """
    Calculate the sum of all numbers in an array using a while loop.
    
    Parameters:
    arr (list): A list of numbers.
    
    Returns:
    int: The sum of all numbers in the array.
    """
    total_sum = 0
    index = 0
    
    while index < len(arr):
        total_sum += arr[index]
        index += 1
    
    return total_sum

# Example usage:
numbers = [1, 2, 3, 4, 5]
print(sum_of_array(numbers))  # Output: 15
