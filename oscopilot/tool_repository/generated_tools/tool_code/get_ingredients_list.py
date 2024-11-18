def get_ingredients_list(recipe_name):
    """
    Get the ingredients list of a specific recipe.

    Args:
        recipe_name (str): The name of the recipe.

    Returns:
        list: A list of ingredients for the recipe.
    """
    # Assuming a dictionary that maps recipe names to their ingredients
    recipe_ingredients = {
        'egg fried rice': ['eggs', 'rice', 'vegetables', 'soy sauce'],
        # Add more recipes as needed
    }

    # Check if the recipe exists in the dictionary
    if recipe_name in recipe_ingredients:
        return recipe_ingredients[recipe_name]
    else:
        return []