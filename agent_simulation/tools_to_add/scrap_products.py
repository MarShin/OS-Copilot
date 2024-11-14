def scrap_products():
    """
    Scrape product data including id, name, price, and packing info.
    
    Args:
    
    Return:
    None
    """

    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium.webdriver.common.by import By
        from selenium_utils.extract_product_data import extract_product_details
        from selenium_utils.json_products_data import save_results_to_json
        import time
        
        # Reconnect to current broswer
        driver = reconnect_driver()
        # Find all product elements
        product_items = driver.find_elements(By.CLASS_NAME, 'product-brief-wrapper')
        results = []

        for item in product_items:
            product_details = extract_product_details(item)
            if product_details:  # Only append if product details were successfully extracted
                results.append(product_details)

        print(f"[{(__name__)}]: Scraped {len(results)} products")
        product_data_save_path = save_results_to_json(results)
        print(f"[{(__name__)}]: Saved the results to json {product_data_save_path}")
        return results
    except Exception as e:
        print(f"[{(__name__)}]:Unable to scrap products: {e}")
        return None
        
