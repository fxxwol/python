class AsciiArt:
    """
    The `AsciiArt` class provides a static method to load ASCII art from a file.

    Methods:
    - `load_ascii_art(file_path: str) -> dict`: Loads ASCII art from a file and returns it as a dictionary.

    Usage example:

    ```python
    file_path = "path/to/ascii_art.txt"
    ascii_dict = AsciiArt.load_ascii_art(file_path)
    ```

    Note: This class is designed to load ASCII art from a file and handle potential errors during the process.
    """

    @staticmethod
    def load_ascii_art(file_path: str) -> dict:
        """
        Loads ASCII art from a file and returns it as a dictionary.

        Parameters:
        - `file_path` (str): The path to the file containing ASCII art.

        Returns:
        dict: A dictionary representing the loaded ASCII art.

        Raises:
        FileNotFoundError: If the specified file is not found.
        Exception: If an error occurs during the loading process.
        """
        try:
            ascii_dict = {}
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read().strip().split("@symbol::")
                for item in content[1:]:
                    symbol, *lines = item.split("\n")
                    ascii_dict[symbol] = [line.strip("^$") for line in lines[0:]]
            return ascii_dict
        except FileNotFoundError:
            print(f"Error: File not found at path '{file_path}'")
        except Exception as e:
            print(f"Error loading ASCII art from '{file_path}': {e}")

