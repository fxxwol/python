from src.classes.file_processor import FileProcessor
from src.classes.input_handling import InputProcessor
from src.classes.ascii_art import ArtSettings
from src.core.lab_4.art_generator import ArtGenerator
from src.core.lab_4.ascii_art import AsciiArt
import os


class ArtGeneratorMenu:
    def __init__(self):
        root = os.getcwd()
        self.symbol_set = {
            "@": os.path.join(root, "src/core/lab_4/art_symbols/dog.txt"),
            "*": os.path.join(root, "src/core/lab_4/art_symbols/asterisk.txt"),
        }
        self.ascii_art = None
        self.settings = None

    def select_symbol(self):
        while True:
            symbol = ArtSettings.choose_symbol("Enter symbol (@ or *):")
            if symbol not in self.symbol_set:
                print("Error! Invalid symbol.")
                continue
            file_path = self.symbol_set[symbol]
            self.ascii_art = AsciiArt.load_ascii_art(file_path)
            break

    def draw_ascii_art(self):
        try:
            self.alignment = ArtSettings.choose_alignment()
            self.max_width = ArtSettings.choose_max_width()
            art_generator = ArtGenerator(self.ascii_art, self.max_width, self.alignment)
            text = art_generator.get_valid_text()
            print("The result of ASCII art:")
            self.ascii_art = art_generator.print_ascii_art(text)
        except ValueError as e:
            print(f"{e}")

    def save(self):
        save_option = InputProcessor.get_yes_no_input(
            "Do you want to save this ASCII art to a file? (yes/no): "
        )
        if save_option.lower() == "yes":
            filename = InputProcessor.get_string_input(
                "Enter the filename to save the ASCII art: "
            )
            file_processor = FileProcessor(filename)
            file_processor.save_art_to_file(self.ascii_art)
            print()

    def run(self):
        self.select_symbol()
        self.draw_ascii_art()
        self.save()
