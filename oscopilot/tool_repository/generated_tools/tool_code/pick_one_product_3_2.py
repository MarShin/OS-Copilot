def pick_one_product_3_2(product_data):
    """
    Pick any one of the product and return its product_code.

    Args:
        product_data (list): A list of dictionaries containing product information.

    Returns:
        str: The product_code of the picked product.
    """
    try:
        if product_data:
            result = product_data[0]['product_code']
        else:
            result = None

        print(f"[{(__name__)}]: Pick the first product with product_code {result}")
        return result
    except Exception as e:
        print(f"[{(__name__)}]: Unable to pick the first products: {e}")
        return None