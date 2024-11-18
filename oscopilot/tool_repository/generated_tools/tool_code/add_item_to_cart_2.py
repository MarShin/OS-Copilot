def add_item_to_cart_2(product_code):
    """
    Add the selected product to cart after pick_one_product.

    Args:
        product_code (str): The product code to be added to cart.

    Returns:
        str: A message indicating whether the product has been successfully added to cart.
    """
    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium.webdriver.common.by import By

        # Reconnect to current browser
        driver = reconnect_driver()
        product = driver.find_element(By.CSS_SELECTOR, f'div[data-id="{product_code}"]')
        add_to_cart_button = product.find_element(By.CLASS_NAME, 'sepaButton.add-to-cart-button')
        add_to_cart_button.click()  # Click the button
        print(f"[{__name__}]Successfully clicked 'Add to Cart' for product code: {product_code}")
        return f"Product {product_code} added to cart successfully."
    except Exception as e:
        print(f"Error adding item to cart: {e}")
        return f"Failed to add product {product_code} to cart."