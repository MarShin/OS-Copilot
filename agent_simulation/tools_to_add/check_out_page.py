def checkout_out_page(btn_class_name="btn-cart"):
    """
    Go to the checkout page of the store.

    Args:
        btn_class_name(str): the class name of the checkout button

    Returns:
    None
    """
    try:
        from selenium_utils.reconnect_driver import reconnect_driver
        from selenium_utils.click_btn import click_btn

        # LLM first create empty brower
        driver = reconnect_driver()

        # Go to check out page
        click_btn(driver, btn_class_name)

    except Exception as e:
        print(f"[{(__name__)}]: {e}")
