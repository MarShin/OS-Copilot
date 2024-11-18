def scrap_products_3():
    """
    Scrap the available products data after searching for a specific product.

    Args:
    None

    Returns:
    The first item of the scraped products list.
    """
    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium.webdriver.common.by import By
        from selenium_utils.extract_product_data import extract_product_details
        from selenium_utils.json_products_data import save_results_to_json
        import time

        # Reconnect to current browser
        driver = reconnect_driver()

        # Find all product elements
        product_items = driver.find_elements(By.CLASS_NAME, 'product-brief-wrapper')
        results = []

        for item in product_items:
            product_details = extract_product_details(item)
            if product_details:  # Only append if product details were successfully extracted
                results.append(product_details)

        print(f"[{(__name__)}]: Scraped {len(results)} products")
        save_results_to_json(results)
        print(f"[{(__name__)}]: Saved the results to json ./product_data/product_data.json")
        if results:
            return results[0]
        else:
            return None

    except Exception as e:
        print(f"[{(__name__)}]: Unable to scrap products: {e}")
        return None