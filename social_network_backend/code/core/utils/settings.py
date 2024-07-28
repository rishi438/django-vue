import os

from .misc import yaml_coerce


def get_settings_from_environment(prefix):
    """
    Extract settings from environment variables based on a prefix.
    Parameters:
        - prefix (str): The prefix used to filter relevant environment variables.
    Returns:
        - dict: A dictionary of settings where keys are derived by removing the
        prefix from environment variable names, and values are coerced from YAML format.
    Example:
        - get_settings_from_environment('APP_') -> {'DEBUG': True, 'PORT': 8080}
    """
    prefix_len = len(prefix)
    return {
        key[prefix_len:]: yaml_coerce(val)
        for key, val in os.environ.items()
        if key.startswith(prefix)
    }
