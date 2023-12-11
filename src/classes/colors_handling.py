import colorama
from colorama import Fore


class ColorProcessor:
    """
    The `ColorProcessor` class provides color-related functionalities using the `colorama` library.

    Attributes:
    - `colors`: A dictionary containing color codes and their corresponding names.

    Methods:
    - `__init__(self)`: Initializes a `ColorProcessor` object, initializing colorama and creating a dictionary of color codes.
    - `display_colors(self)`: Displays a list of available color codes and their names.
    - `get_colors(self) -> dict`: Returns the dictionary containing color codes and their names.

    Usage example:

    ```python
    color_processor = ColorProcessor()
    color_processor.display_colors()
    available_colors = color_processor.get_colors()
    ```

    Note: This class relies on the `colorama` library for color handling.
    """

    def __init__(self):
        """
        Initializes a ColorProcessor object, initializing colorama and creating a dictionary of color codes.
        """
        colorama.init(autoreset=True)
        self.colors = dict(enumerate(sorted(Fore.__dict__.keys())))

    def display_colors(self):
        """
        Displays a list of available color codes and their names.
        """
        for i in self.colors:
            print(str(i) + ". " + self.colors[i])

    def get_colors(self) -> dict:
        """
        Returns the dictionary containing color codes and their names.

        Returns:
        dict: A dictionary containing color codes and their names.
        """
        return self.colors
