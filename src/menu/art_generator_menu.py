
from core.lab_4.art_generator import ArtGenerator
from core.lab_4.art_settings import Settings
from core.lab_4.ascii_art import AsciiArt
from core.lab_4.interactions import UserInteraction
from menu.art_menu import ArtMenu
from utils.input_handling import get_string_input, get_integer_input, get_yes_no_input
import os


class AsciiArtGeneratorMenu(ArtMenu):
    def run(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        symbol_set = {
            "@": os.path.join(script_dir, "art_symbols/dog.txt"),
            "*": os.path.join(script_dir, "art_symbols/asterisk.txt"),
        }

        while True:
            options = {"1": "Select a symbol", "0": "Exit"}
            option = self.get_option(options)

            if option == "1":
                selected_symbol = get_string_input("Select a symbol ( @, *): ")
                if selected_symbol not in symbol_set:
                    print("Error! Invalid symbol.")
                    continue

                file_path = symbol_set[selected_symbol]
                ascii_art = AsciiArt.load_ascii_art(file_path)

                while True:
                    color = UserInteraction.select_color()
                    if color is None:
                        continue

                    alignment = get_string_input(
                        "Select alignment (left, center, right): "
                    ).lower()
                    if alignment not in ["left", "center", "right"]:
                        print("Error! Invalid alignment.")
                        continue

                    max_width = get_integer_input("Enter maximum width: ")

                    try:
                        settings = Settings(max_width, alignment)
                        art_generator = ArtGenerator(ascii_art, settings)
                        text = art_generator.get_valid_text()
                        print("The result of ASCII art:")
                        art = art_generator.print_ascii_art(text, color)

                        save_choice = get_yes_no_input(
                            "Do you want to save the ASCII art to a text file? (yes/no): "
                        )
                        if save_choice == "yes":
                            filename = get_string_input("Enter file name")
                            art_generator.save_to_text_file(art, filename)
                            print("ASCII art saved to", filename)

                        continue_choice = get_yes_no_input(
                            "Do you want to continue drawing ASCII art? (yes/no): "
                        )
                        if continue_choice != "yes":
                            exit()
                    except ValueError as e:
                        print(e)

            elif option == "0":
                exit()

            else:
                print("Invalid option!")

