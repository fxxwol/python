from colorama import Fore
from src.classes.colors_handling import ColorProcessor


class JSONFlattener:
    """
    The `JSONFlattener` class provides methods for flattening JSON data and displaying the flattened results.

    Methods:
    - `flatten_json(json_data: dict, parent_key: str = "", delimiter="_") -> dict`: Flattens nested JSON data.
    - `display_flattened_json(jsons, color_position: int = 4)`: Displays flattened JSON data with colorized output.

    Usage example:

    ```python
    json_flattener = JSONFlattener()
    json_data = {"name": "John", "address": {"city": "New York", "zip": "10001"}}
    flattened_data = json_flattener.flatten_json(json_data)
    json_flattener.display_flattened_json(flattened_data, color_position=2)
    ```

    Note: This class is designed to handle JSON flattening and display with colorized output.
    """

    @staticmethod
    def flatten_json(json_data: dict, parent_key: str = "", delimiter="_") -> dict:
        """
        Flattens nested JSON data.

        Parameters:
        - `json_data` (dict): The nested JSON data to be flattened.
        - `parent_key` (str): The parent key used for building the flattened keys.
        - `delimiter` (str): The delimiter used to separate keys in the flattened structure.

        Returns:
        dict: The flattened JSON data.
        """
        if (
            not isinstance(json_data, dict)
            and not isinstance(parent_key, str)
            and not isinstance(delimiter, str)
        ):
            raise ValueError("Wrong data types!")

        flat_data = {}
        for key, value in json_data.items():
            new_key = parent_key + delimiter + key if parent_key else key

            if isinstance(value, dict):
                flat_data.update(JSONFlattener.flatten_json(value, new_key, delimiter))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    flat_data.update(
                        JSONFlattener.flatten_json({str(i): item}, new_key, delimiter)
                    )
            else:
                flat_data[new_key] = value

        return flat_data

    @staticmethod
    def display_flattened_json(jsons, color_position: int = 4):
        """
        Displays flattened JSON data with colorized output.

        Parameters:
        - `jsons`: The JSON data to be displayed.
        - `color_position` (int): The position of the color in the ColorProcessor.

        Raises:
        - `ValueError`: If the data types or color position are incorrect.

        Note:
        - The color position should be an integer between 0 and the maximum color index.
        """
        if (
            not isinstance(jsons, dict) and not isinstance(jsons, list)
        ) or not isinstance(color_position, int):
            raise ValueError("Wrong data types!")
        elif color_position < 0 or color_position > len(ColorProcessor.colors):
            raise ValueError("Wrong color position!")

        color = Fore.__getattribute__(ColorProcessor.colors[color_position])

        if isinstance(jsons, list):
            for counter, json_data in enumerate(jsons):
                flat_json = JSONFlattener.flatten_json(json_data)
                for key, value in flat_json.items():
                    print(f"{color}{key}:{Fore.RESET} {value}")
        elif isinstance(jsons, dict):
            flat_json = JSONFlattener.flatten_json(jsons)
            for key, value in flat_json.items():
                print(f"{color}{key}:{Fore.RESET} {value}")
