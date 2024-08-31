import math

def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * (radius ** 2)

def main():
    try:
        # Get user input for the radius
        radius = float(input("Enter the radius of the circle: "))
        
        if radius <= 0:
            print("Radius must be a positive number.")
        else:
            # Calculate and display the area
            area = calculate_circle_area(radius)
            print(f"The area of the circle is {area:.2f} square units.")
    
    except ValueError:
        print("Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()
