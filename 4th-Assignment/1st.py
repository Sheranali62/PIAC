from datetime import datetime

def calculate_age(birth_year):
    # Get the current year
    current_year = datetime.now().year
    
    # Calculate age
    age = current_year - birth_year
    
    return age

def main():
    # Ask the user for their birth year
    try:
        birth_year = int(input("Enter your birth year: "))
        if birth_year > datetime.now().year:
            print("Birth year cannot be in the future.")
        else:
            # Calculate and display age
            age = calculate_age(birth_year)
            print(f"You are {age} years old.")
    except ValueError:
        print("Please enter a valid year.")

if __name__ == "__main__":
    main()
