def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def main():
    try:
        # Get user input for length and width
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers.")
        else:
            # Calculate and display the area
            area = calculate_rectangle_area(length, width)
            print(f"The area of the rectangle is {area:.2f} square units.")
    
    except ValueError:
        print("Please enter valid numbers for length and width.")

if __name__ == "__main__":
    main()
