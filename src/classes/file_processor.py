import pandas as pd
import os
import json
from requests import JSONDecodeError


class FileProcessor:
    def __init__(self, file_path):
        self.save_file_path = os.path.join(
            os.getcwd(), "src", "results", "exported_diagram.png"
        )
        self.file_path = file_path

    def save_to_file(self, data):
        try:
            os.makedirs(self.file_path, exist_ok=True)
            with open(self.file_path, "w") as file:
                file.write(data)
            print(f"Data saved to {self.save_file_path}")
        except IOError as e:
            print(f"Error saving data to {self.save_file_path}: {e}")

    def read_from_file(self):
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

    def write_into_json(self, jsons):
        jsons_text_representation = JSONDecodeError.dumps(jsons, indent=4)
        json.loads(jsons_text_representation)
        self.save_to_file(jsons_text_representation)

    def csv_load(self):
        data = pd.read_csv(self.file_path)
        return data
