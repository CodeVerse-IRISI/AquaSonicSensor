"""
Module to read configuration from a JSON file.
"""

import json


def read_config(config_file, prop_name):
    """
    Read a property from a JSON configuration file.

    Args:
        config_file (str): Path to the JSON configuration file.
        prop_name (str): Name of the property to read.

    Returns:
        str: Value of the property.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        KeyError: If the property is not found in the configuration file.
        ValueError: If the configuration file has invalid JSON format.
    """
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
            prop_value = config_data.get(prop_name)
            if prop_value is None:
                raise KeyError(f"Property '{prop_name}' not found in the configuration file.")
            return prop_value
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON format in configuration file '{config_file}'.") from exc
