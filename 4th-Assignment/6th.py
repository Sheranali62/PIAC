def convert_seconds(seconds):
    """Convert seconds into minutes and seconds."""
    minutes = seconds // 60       # Integer division to get the number of minutes
    remaining_seconds = seconds % 60  # Modulus to get the remaining seconds
    
    return minutes, remaining_seconds

def main():
    try:
        # Get user input for the number of seconds
        total_seconds = int(input("Enter the number of seconds: "))
        
        if total_seconds < 0:
            print("The number of seconds cannot be negative.")
        else:
            # Convert seconds to minutes and seconds
            minutes, remaining_seconds = convert_seconds(total_seconds)
            print(f"{total_seconds} seconds is equivalent to {minutes} minute(s) and {remaining_seconds} second(s).")
    
    except ValueError:
        print("Please enter a valid number for seconds.")

if __name__ == "__main__":
    main()
