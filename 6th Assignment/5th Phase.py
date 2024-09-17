def factorial(n):
    """
    Calculate the factorial of a positive integer n using a while loop.
    
    Parameters:
    n (int): A positive integer whose factorial is to be calculated.
    
    Returns:
    int: The factorial of the given number.
    """
    if n < 0:
        raise ValueError("Input must be a positive integer")
    
    result = 1
    
    while n > 0:
        result *= n
        n -= 1
    
    return result

# Example usage:
print(factorial(5))  # Output: 120
