def print_cart(cart):
    """Prints the contents of the shopping cart."""
    if not cart:
        print("The cart is empty.")
    else:
        print("Shopping Cart Contents:")
        for item in cart:
            print(f"{item['name']} - Quantity: {item['quantity']}")
    print()

def add_item(cart, name, quantity):
    """Adds an item to the cart. If the item already exists, updates the quantity."""
    for item in cart:
        if item['name'] == name:
            item['quantity'] += quantity
            print(f"Updated {name} quantity to {item['quantity']}.")
            print_cart(cart)
            return
    # If item is not found, add it to the cart
    cart.append({'name': name, 'quantity': quantity})
    print(f"Added {name} with quantity {quantity}.")
    print_cart(cart)

def remove_item(cart, name):
    """Removes an item from the cart by its name."""
    for item in cart:
        if item['name'] == name:
            cart.remove(item)
            print(f"Removed {name} from the cart.")
            print_cart(cart)
            return
    print(f"Item {name} not found in the cart.")
    print_cart(cart)

def update_quantity(cart, name, quantity):
    """Updates the quantity of an existing item in the cart."""
    for item in cart:
        if item['name'] == name:
            if quantity <= 0:
                print(f"Quantity must be greater than zero. Item {name} not updated.")
                return
            item['quantity'] = quantity
            print(f"Updated {name} quantity to {quantity}.")
            print_cart(cart)
            return
    print(f"Item {name} not found in the cart.")
    print_cart(cart)

# Initialize the shopping cart
shopping_cart = []

# Example operations
add_item(shopping_cart, 'Apple', 3)
add_item(shopping_cart, 'Banana', 2)
update_quantity(shopping_cart, 'Apple', 5)
remove_item(shopping_cart, 'Banana')
add_item(shopping_cart, 'Orange', 4)
update_quantity(shopping_cart, 'Orange', 6)  # Invalid update, should show error message
