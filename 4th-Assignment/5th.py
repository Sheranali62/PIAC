def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def main():
    try:
        # Get the conversion direction from the user
        direction = input("Enter 'F to C' to convert Fahrenheit to Celsius or 'C to F' to convert Celsius to Fahrenheit: ").strip().upper()
        
        if direction not in ['F TO C', 'C TO F']:
            print("Invalid option. Please enter 'F to C' or 'C to F'.")
            return
        
        # Get temperature value from the user
        temperature = float(input("Enter the temperature to convert: "))
        
        if direction == 'F TO C':
            # Convert Fahrenheit to Celsius
            converted = fahrenheit_to_celsius(temperature)
            print(f"{temperature} Fahrenheit is {converted:.2f} Celsius.")
        else:
            # Convert Celsius to Fahrenheit
            converted = celsius_to_fahrenheit(temperature)
            print(f"{temperature} Celsius is {converted:.2f} Fahrenheit.")
    
    except ValueError:
        print("Please enter a valid number for the temperature.")

if __name__ == "__main__":
    main()
