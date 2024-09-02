def analyze_number(num):
    # Check if the number is even or odd
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")
    
    # Check if the number is positive, negative, or zero
    if num > 0:
        print(f"{num} is Positive.")
    elif num < 0:
        print(f"{num} is Negative.")
    else:
        print(f"{num} is Zero.")
    
    # Check if the number is divisible by both 2 and 3, only one of them, or neither
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num} is divisible by both 2 and 3.")
    elif num % 2 == 0:
        print(f"{num} is divisible by 2 only.")
    elif num % 3 == 0:
        print(f"{num} is divisible by 3 only.")
    else:
        print(f"{num} is not divisible by either 2 or 3.")

# Example usage
number = int(input("Enter a number: "))
analyze_number(number)
