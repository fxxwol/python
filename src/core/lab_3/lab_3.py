import pyfiglet
from termcolor import colored
from src.menu.ascii_art_menu import AsciiArtMenu

# Function to format ASCII art by replacing '#' with a custom symbol
def format_ascii_art(art, symbol):
    return art.replace("#", symbol)


# Function to resize ASCII art to a specified width and height
def resize_ascii_art(ascii_art, width, height):
    # Split the ASCII art into lines
    lines = ascii_art.split("\n")

    # Resize the ASCII art to the specified height
    while len(lines) < height:
        lines.append(" " * len(lines[0]))

    # Resize each line to the specified width
    for i in range(len(lines)):
        lines[i] = lines[i].ljust(width)[:width]

    return "\n".join(lines)


# Main function
def main():
    menu = AsciiArtMenu()
    user_input = menu.get_user_input()
    selected_font = menu.choose_font()
    symbol = menu.choose_symbol()

    ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)

    formatted_art = format_ascii_art(ascii_art, symbol)
    print(formatted_art)

    menu.resize_ascii_art()

    width = menu.width
    height = menu.height

    resized_art = resize_ascii_art(formatted_art, width, height)

    print(resized_art)

    menu.save(resized_art)


if __name__ == "__main__":
    main()