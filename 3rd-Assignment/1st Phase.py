import math

def calculate_cylinder_volume(radius, height):
    """Calculate the volume of a cylinder given its radius and height."""
    if radius <= 0 or height <= 0:
        return "Radius and height must be positive numbers."
    volume = math.pi * (radius ** 2) * height
    return volume

def main():
    try:
        # Get user input for radius and height
        radius = float(input("Enter the radius of the cylinder (in meters): "))
        height = float(input("Enter the height of the cylinder (in meters): "))
        
        # Calculate volume
        volume = calculate_cylinder_volume(radius, height)
        
        if isinstance(volume, str):
            print(volume)
        else:
            # Display the volume
            print(f"The volume of the cylinder is: {volume:.2f} cubic meters")
                
    except ValueError:
        print("Invalid input. Please enter numeric values for radius and height.")

if __name__ == "__main__":
    main()
