import yaml


def yaml_coerce(val):
    """
    Converts a given string from YAML format to a proper Python data type.
    Parameters:
        - val (str or other type): The value to be converted. If it is
        a string, it will be processed as a YAML value.
    Returns:
        - Any: The converted Python value if input is a string, or the
        soriginal value if it is of other types.
    Example:
        - yaml_coerce("42") -> 42
    """
    # convert to proper Python

    if isinstance(val, str):
        return yaml.load(f"dummy: {val}", Loader=yaml.SafeLoader)["dummy"]
    return val
