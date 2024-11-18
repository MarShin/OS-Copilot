def search_products_3(text):
    """
    Search products by locating the search bar, inputting the text, and clicking enter.

    Args:
        text (str): The products to search.

    Returns:
        None
    """
    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        import time

        # Reconnect to current browser
        driver = reconnect_driver()
        search_input = driver.find_element(By.CLASS_NAME, "SuggestionSearch-input")
        search_input.clear()  # Clear any existing text
        search_input.send_keys(text)  # Type the search text
        search_input.send_keys(Keys.RETURN)  # Click enter
        time.sleep(2)
        print(f"[{(__name__)}]: successfully searched: {text}")

    except Exception as e:
        print(f"[{(__name__)}]: Error occurred during the search: {e}")