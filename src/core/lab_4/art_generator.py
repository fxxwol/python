class ArtGenerator:
    """
    The `ArtGenerator` class provides methods for generating and displaying ASCII art based on user input.

    Methods:
    - `__init__(ascii_dict, max_width, alignment)`: Initializes an `ArtGenerator` object with ASCII dictionary, maximum width, and alignment.
    - `get_valid_text() -> str`: Prompts the user to enter a word or phrase, ensuring it contains valid characters.
    - `print_ascii_art(text) -> List[str]`: Generates and displays ASCII art based on the input text.

    Usage example:

    ```python
    ascii_dict = {"A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"]}
    max_width = 10
    alignment = "center"
    art_generator = ArtGenerator(ascii_dict, max_width, alignment)
    user_text = art_generator.get_valid_text()
    art_lines = art_generator.print_ascii_art(user_text)
    ```

    Note: This class is designed to handle ASCII art generation and display with user input validation.
    """

    def __init__(self, ascii_dict, max_width, alignment):
        """
        Initializes an `ArtGenerator` object.

        Parameters:
        - `ascii_dict` (dict): A dictionary containing ASCII representations of symbols.
        - `max_width` (int): The maximum width for the ASCII art.
        - `alignment` (str): The alignment of the ASCII art ('left', 'center', or 'right').
        """
        self.ascii_dict = ascii_dict
        self.max_width = max_width
        self.alignment = alignment

    def get_valid_text(self):
        """
        Prompts the user to enter a word or phrase, ensuring it contains valid characters.

        Returns:
        str: The user-entered text.

        Raises:
        ValueError: If the input contains invalid characters.
        """
        while True:
            text = input("Enter a word or phrase: ")
            if all(c in self.ascii_dict or c == " " for c in text):
                return text
            else:
                raise ValueError(
                    "Error. The input contains invalid characters. Please enter a valid phrase."
                )

    def print_ascii_art(self, text):
        """
        Generates and displays ASCII art based on the input text.

        Parameters:
        - `text` (str): The text for which ASCII art is generated and displayed.

        Returns:
        List[str]: The lines of the generated ASCII art.

        Raises:
        ValueError: If the maximum width is too small for the input phrase.
        """
        output_lines = [""] * 6

        for symbol in text:
            if symbol == " ":
                for i in range(6):
                    output_lines[i] += " "
            elif symbol in self.ascii_dict:
                symbol_lines = self.ascii_dict[symbol]
                for i in range(6):
                    output_lines[i] += symbol_lines[i]

        if len(output_lines[0]) > self.max_width:
            raise ValueError("Error. Maximum width is too small for the input phrase.")

        if self.alignment == "center":
            output_lines = [line.center(self.max_width) for line in output_lines]
        elif self.alignment == "right":
            output_lines = [line.rjust(self.max_width) for line in output_lines]

        for line in output_lines:
            print(line)
        return output_lines
