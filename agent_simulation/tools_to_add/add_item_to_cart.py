def add_item_to_cart(product_code):
    """
    Add the item with the specified product code to the cart.
    
    Args:
        product_code(str): the product id to be added to cart
    
    Return:
    None
        
    """
    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium.webdriver.common.by import By

        # Reconnect to current broswer
        driver = reconnect_driver()
        product = driver.find_element(By.CSS_SELECTOR, f'div[data-id="{product_code}"]')
        add_to_cart_button = product.find_element(By.CLASS_NAME, 'sepaButton.add-to-cart-button')
        add_to_cart_button.click()  # Click the button
        print(f"[{__name__}]Clicked 'Add to Cart' for product code: {product_code}")
    except Exception as e:
        print(f"Error adding item to cart: {e}")
        
