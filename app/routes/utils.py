def calculate_total_price(cart_items):
    """
    Calculate the total price of items in the cart.

    Args:
        cart_items: List of cart items, where each item is a dictionary containing 'product' and 'quantity' keys.

    Returns:
        float: Total price of all items in the cart.
    """
    total_price = sum(item['product'].price * item['quantity'] for item in cart_items)
    return total_price
