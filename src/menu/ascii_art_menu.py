from menu.art_menu import ArtMenu
import pyfiglet
from termcolor import colored

class AsciiArtMenu(ArtMenu):
    def run(self):
        user_input = self.get_user_input()
        selected_font = self.choose_font()
        selected_color = self.choose_color()
        symbol = self.choose_symbol()

        # Generate ASCII art using pyfiglet and color it
        ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
        colored_art = colored(ascii_art, color=selected_color)

        # Format the ASCII art with the chosen symbol
        formatted_art = self.format_ascii_art(colored_art, symbol)

        print(formatted_art)

        # Get user input for desired width and height
        width = self.get_integer_input("Enter the desired width (number of columns): ")
        height = self.get_integer_input("Enter the desired height (number of rows): ")

        # Resize the ASCII art
        resized_art = self.resize_ascii_art(formatted_art, width, height)

        print(resized_art)

        # Ask the user if they want to save the ASCII art to a file
        save_option = self.get_string_input(
            "Do you want to save this ASCII art to a file? (yes/no): "
        )
        if save_option.lower() == "yes":
            file_name = self.choose_file_path()
            self.save_to_file(file_name, resized_art)
