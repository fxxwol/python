class AsciiArt:
    @staticmethod
    def load_ascii_art(file_path):
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
