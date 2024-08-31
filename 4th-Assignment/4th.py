def calculate_cube_surface_area(side):
    """Calculate the surface area of a cube."""
    return 6 * (side ** 2)

def main():
    try:
        # Get user input for the side length of the cube
        side = float(input("Enter the length of a side of the cube: "))
        
        if side <= 0:
            print("Side length must be a positive number.")
        else:
            # Calculate and display the surface area
            surface_area = calculate_cube_surface_area(side)
            print(f"The surface area of the cube is {surface_area:.2f} square units.")
    
    except ValueError:
        print("Please enter a valid number for the side length.")

if __name__ == "__main__":
    main()
