def days_in_month(month):
    # Define the number of days in each month for a non-leap year
    days_per_month = {
        1: 31,  # January
        2: 28,  # February (non-leap year)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31, # October
        11: 30, # November
        12: 31  # December
    }
    
    if 1 <= month <= 12:
        return days_per_month[month]
    else:
        return "Invalid month. Please enter a number between 1 and 12."

def is_leap_year(year):
    # A year is a leap year if:
    # - It is divisible by 4
    # - It is not divisible by 100, except if it is also divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def main():
    # Get the month from the user and display the number of days
    month = int(input("Enter a month (1-12): "))
    days = days_in_month(month)
    if isinstance(days, int):
        print(f"The number of days in month {month} is {days}.")
    else:
        print(days)
    
    # Get the year from the user and check if it is a leap year
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

# Run the main function
main()
