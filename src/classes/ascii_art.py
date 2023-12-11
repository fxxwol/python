from src.classes.colors_handling import ColorProcessor
from src.classes.file_processor import FileProcessor
from src.classes.input_handling import InputProcessor


class ArtSettings:
    """
    The `ArtSettings` class provides methods for configuring ASCII art settings.

    Methods:
    - `choose_max_width()`: Allows the user to enter the maximum width for ASCII art.
    - `choose_alignment()`: Allows the user to select the alignment for ASCII art (left, center, right).
    - `choose_symbol(prompt="Enter a symbol: ")`: Allows the user to enter a symbol fo ASCII art.
    - `choose_color()`: Allows the user to select a color for ASCII art.
    - `save_to_file(content)`: Asks the user if they want to save the ASCII art to a file and, if yes,
       prompts for a filename and saves the content to the specified file.

    Usage example:

    ```python
    settings = ArtSettings()
    max_width = settings.choose_max_width()
    alignment = settings.choose_alignment()
    symbol = settings.choose_symbol()
    color = settings.choose_color()

    # Perform some actions with the chosen settings...

    content = "Your ASCII art content here."
    settings.save_to_file(content)
    ```

    Note: This class relies on the `InputProcessor`, `ColorProcessor`, and `FileProcessor` classes for user input,
    color handling, and file operations, respectively.
    """

    @staticmethod
    def choose_max_width():
        """
        Prompt the user to enter the maximum width for ASCII art.

        Returns:
        int: The chosen maximum width.
        """
        return InputProcessor.get_integer_input("Enter maximum width: ")

    @staticmethod
    def choose_alignment():
        """
        Prompt the user to select the alignment for ASCII art (left, center, right).

        Returns:
        str: The chosen alignment.
        Raises:
        ValueError: If an invalid alignment is entered.
        """
        while True:
            try:
                chosen_alignment = InputProcessor.get_string_input(
                    "Select alignment (left, center, right): "
                ).lower()
                if chosen_alignment not in ["left", "center", "right"]:
                    raise ValueError("Error! Invalid alignment.")
                return chosen_alignment
            except ValueError:
                print("Invalid input. Please enter a valid alignment.")

    @staticmethod
    def choose_symbol(prompt="Enter a symbol: "):
        """
        Prompt the user to enter a symbol for customizing ASCII art.

        Parameters:
        prompt (str): Custom prompt for symbol entry.

        Returns:
        str: The chosen symbol.
        """
        return InputProcessor.get_string_input(prompt)

    @staticmethod
    def choose_color():
        """
        Prompt the user to select a color for ASCII art.

        Returns:
        int: The chosen color position.
        Raises:
        ValueError: If an invalid color position is entered.
        """
        colors = ColorProcessor().get_colors()
        print("Available colors:")
        ColorProcessor().display_colors()
        while True:
            try:
                color_choice = InputProcessor.get_integer_input(
                    "Select a color (enter the corresponding number): "
                )
                if color_choice not in colors:
                    raise ValueError(
                        "Color position must be in the range of available colors"
                    )
                return color_choice
            except ValueError:
                print("Invalid input. Please enter a valid color choice.")

    @staticmethod
    def save_to_file(content):
        """
        Ask the user if they want to save the ASCII art to a file.
        If yes, prompt for a filename and save the content to the specified file.

        Parameters:
        content (str): The ASCII art content to be saved.
        """
        save_option = InputProcessor.get_yes_no_input(
            "Do you want to save this ASCII art to a file? (yes/no): "
        )
        if save_option.lower() == "yes":
            filename = InputProcessor.get_string_input(
                "Enter the filename to save the ASCII art: "
            )
            file_processor = FileProcessor(filename)
            file_processor.save_to_file(content)
