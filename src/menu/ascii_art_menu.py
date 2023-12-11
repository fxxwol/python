import pyfiglet
from src.classes.ascii_art import ArtSettings
from src.classes.input_handling import InputProcessor


class AsciiArtMenu:
    def __init__(self):
        self.user_input = None
        self.selected_font = None
        self.selected_color = None
        self.symbol = None
        self.ascii_art = None
        self.width = None
        self.height = None

    def get_user_input(self):
        return InputProcessor.get_string_input("Enter a word or phrase: ")

    def choose_font(self):
        available_fonts = pyfiglet.FigletFont.getFonts()
        print("Available fonts:")
        for font in available_fonts:
            print(font)
        try:
            chosen = InputProcessor.get_string_input("Choose a font: ")
            if not available_fonts.__contains__(chosen):
                raise ValueError("Font foesn't exist")
            return chosen
        except ValueError:
            print("Font foesn't exist")

    def choose_color(self):
        return ArtSettings.choose_color()

    def choose_symbol(self):
        return ArtSettings.choose_symbol()

    def resize_ascii_art(self):
        self.width = InputProcessor.get_integer_input(
            "Enter the desired width (number of columns): "
        )
        self.height = InputProcessor.get_integer_input(
            "Enter the desired height (number of rows): "
        )

    def save(self, art):
        ArtSettings.save_to_file(art)
