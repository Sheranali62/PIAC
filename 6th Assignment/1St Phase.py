def insert_at_index(array, index, value):

    # Handle negative index and ensure index is within bounds
    if index < 0:
        index = max(0, len(array) + index + 1)
    else:
        index = min(len(array), index)

    # Create the new list by concatenating slices and the new value
    return array[:index] + [value] + array[index:]

# Example usage
my_list = [1, 2, 3, 4]
index = 2
value = 'a'

# Call the function
modified_list = insert_at_index(my_list, index, value)

print(modified_list)  # Output: [1, 2, 'a', 3, 4]
