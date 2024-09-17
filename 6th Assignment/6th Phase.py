def remove_negatives(arr):
    """
    Remove negative numbers from an array.
    
    Parameters:
    arr (list): A list of numbers.
    
    Returns:
    list: A new list with negative numbers removed.
    """
    index = 0
    while index < len(arr):
        if arr[index] < 0:
            arr.pop(index)
        else:
            index += 1
    return arr

# Example usage:
numbers = [10, -1, 2, -3, 4, -5]
print(remove_negatives(numbers))  # Output: [10, 2, 4]
