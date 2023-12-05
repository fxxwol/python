import json
import pandas

pandas.set_option("display.max_rows", None)
pandas.set_option("display.max_columns", None)


def write_into_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()


def read_from_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)


def write_into_json(file_path: str, jsons: list) -> None:
    jsons_text_representation = json.dumps(jsons, indent=4)
    json.loads(jsons_text_representation)

    with open(file_path, "w") as file:
        file.write(jsons_text_representation)


class CsvProcessor:
    @staticmethod
    def read(file_path: str) -> pandas.DataFrame:
        return pandas.read_csv(file_path)
