def calculate_percentage(part, whole):
    """Calculate the percentage of part out of whole."""
    if whole == 0:
        return None  # Avoid division by zero
    return (part / whole) * 100

def main():
    try:
        # Get user input for the part and whole
        part = float(input("Enter the part: "))
        whole = float(input("Enter the whole: "))
        
        if whole <= 0:
            print("The whole value must be greater than zero.")
        else:
            # Calculate percentage
            percentage = calculate_percentage(part, whole)
            print(f"{part} is {percentage:.2f}% of {whole}.")
    
    except ValueError:
        print("Please enter valid numbers for part and whole.")

if __name__ == "__main__":
    main()
