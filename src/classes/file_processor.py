import pandas as pd
import os
import json


class FileProcessor:
    """
    The `FileProcessor` class provides methods for reading from and saving data to files,
    specifically designed for handling various types of data such as plain text, JSON, and CSV.

    Attributes:
    - `save_file_path`: The full path to the directory where the file will be saved.
    - `file_path`: The relative path to the file being processed.

    Methods:
    - `__init__(self, file_path)`: Initializes a `FileProcessor` object with the provided file path.
    - `save_to_file(self, data)`: Saves data to a plain text file.
    - `read_from_file(self) -> dict`: Reads data from a plain text file and returns it as a dictionary.
    - `save_art_to_file(self, data)`: Saves ASCII art data to a plain text file.
    - `write_into_json(self, jsons)`: Writes JSON-formatted data into a file.
    - `csv_load(self) -> pd.DataFrame`: Loads data from a CSV file into a Pandas DataFrame.

    Usage example:

    ```python
    file_processor = FileProcessor("example.txt")
    data_to_save = "Hello, World!"
    file_processor.save_to_file(data_to_save)

    loaded_data = file_processor.read_from_file()
    print(loaded_data)

    json_data = {"key": "value"}
    file_processor.write_into_json(json_data)

    csv_data = file_processor.csv_load()
    print(csv_data)
    ```

    Note: This class is designed to handle plain text, JSON, and CSV file operations.
    """

    def __init__(self, file_path):
        """
        Initializes a FileProcessor object with the provided file path.

        Parameters:
        - `file_path` (str): The relative path to the file being processed.
        """
        self.save_file_path = os.path.join(os.getcwd(), "src", "results", file_path)
        self.file_path = file_path

    def save_to_file(self, data):
        """
        Saves data to a plain text file.

        Parameters:
        - `data` (str): The data to be saved.
        """
        try:
            with open(self.save_file_path, "w") as file:
                file.write(data)
            print(f"Data saved to {self.save_file_path}")
        except IOError as e:
            print(f"Error saving data to {self.save_file_path}: {e}")

    def read_from_file(self) -> dict:
        """
        Reads data from a plain text file and returns it as a dictionary.

        Returns:
        dict: The data read from the file as a dictionary.
        None: If an error occurs during file reading.
        """
        try:
            with open(self.file_path, "r") as file:
                data = {}
                for line in file:
                    key, value = line.strip().split(": ")
                    data[key] = value
            print(f"Data loaded from {self.file_path}")
            return data
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
            return None
        except IOError as e:
            print(f"Error reading data from {self.file_path}: {e}")
            return None

    def save_art_to_file(self, data):
        """
        Saves ASCII art data to a plain text file.

        Parameters:
        - `data` (list): List of ASCII art lines to be saved.
        """
        try:
            with open(self.save_file_path, "w") as file:
                for line in data:
                    file.write(line + "\n")
            print(f"Data saved to {self.save_file_path}")
        except IOError as e:
            print(f"Error saving data to {self.save_file_path}: {e}")

    def write_into_json(self, jsons):
        """
        Writes JSON-formatted data into a file.

        Parameters:
        - `jsons` (dict): The data to be written in JSON format.
        """
        jsons_text_representation = json.dumps(jsons, indent=4)
        json.loads(jsons_text_representation)
        self.save_to_file(jsons_text_representation)

    def csv_load(self) -> pd.DataFrame:
        """
        Loads data from a CSV file into a Pandas DataFrame.

        Returns:
        pd.DataFrame: The loaded data as a Pandas DataFrame.
        """
        data = pd.read_csv(self.file_path)
        return data
