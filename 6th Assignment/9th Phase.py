def remove_odd_numbers(numbers_list):
    index = 0
    while index < len(numbers_list):
        if numbers_list[index] % 2 != 0:  # Check if the number is odd
            numbers_list.pop(index)  # Remove the odd number
        else:
            index += 1  # Move to the next number if no removal
    return numbers_list

def main():
    numbers_input = input("Enter numbers separated by commas (e.g., 1, 2, 3, 4, 5): ")
    numbers_list = [int(num.strip()) for num in numbers_input.split(',')]
    
    even_numbers_list = remove_odd_numbers(numbers_list)
    
    print("Numbers after removing odd ones:", even_numbers_list)

if __name__ == "__main__":
    main()
