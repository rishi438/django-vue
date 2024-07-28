def deep_update(base_dict, update_dict):
    """
    Recursively updates a nested dictionary with another dictionary's key-value pairs.

    Parameters:
        - base_dict (dict): The dictionary to be updated.
        - update_dict (dict): The dictionary with updates.

    Returns:
        - dict: The updated dictionary.

    Example:
        - deep_update({'a': {'b': 1}}, {'a': {'c': 2}}) -> {'a': {'b': 1, 'c': 2}}
    """
    for key, value in update_dict.items():
        if isinstance(value, dict) and isinstance(base_dict.get(key), dict):
            deep_update(base_dict[key], value)
        else:
            base_dict[key] = value
    return base_dict
