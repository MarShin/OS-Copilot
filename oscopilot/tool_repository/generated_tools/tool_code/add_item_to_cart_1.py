def add_item_to_cart_1(pick_one_product_return_val):
    """
    Add the selected product to cart after pick_one_product.

    Args:
        pick_one_product_return_val (dict): The return value of pick_one_product, containing the product code.

    Returns:
        str: A message indicating whether the product was successfully added to the cart.
    """
    product_code = pick_one_product_return_val['product_code']
    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # Reconnect to current browser
        driver = reconnect_driver()
        product = driver.find_element(By.CSS_SELECTOR, f'div[data-id="{product_code}"]')
        add_to_cart_button = product.find_element(By.CLASS_NAME, "add-to-cart-button")

        # Wait for the button to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(add_to_cart_button))

        # Move to the button and click it
        driver.execute_script("arguments[0].click();", add_to_cart_button)

        print(f"[{__name__}]Successfully clicked Add to Cart for product code: {product_code}")
        return f"Product {product_code} added to cart successfully."
    except Exception as e:
        print(f"Error adding item to cart: {e}")
        return f"Failed to add product {product_code} to cart."