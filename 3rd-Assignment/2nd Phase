def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    if height <= 0 or weight <= 0:
        return "Height and weight must be positive numbers."
    bmi = weight / (height ** 2)
    return bmi

def main():
    try:
        # Get user input for height and weight
        height = float(input("Enter your height in meters: "))
        weight = float(input("Enter your weight in kilograms: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        if isinstance(bmi, str):
            print(bmi)
        else:
            # Display BMI and its category
            print(f"Your BMI is: {bmi:.2f}")
            
            if bmi < 18.5:
                print("Category: Underweight")
            elif 18.5 <= bmi < 24.9:
                print("Category: Normal weight")
            elif 25 <= bmi < 29.9:
                print("Category: Overweight")
            else:
                print("Category: Obesity")
                
    except ValueError:
        print("Invalid input. Please enter numeric values for height and weight.")

if __name__ == "__main__":
    main()
