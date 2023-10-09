import pyfiglet
from termcolor import colored

def get_user_input():
    user_input = input("Enter a word or phrase: ")
    return user_input

def choose_font():
    available_fonts = pyfiglet.FigletFont.getFonts()
    print("Available fonts:")
    for font in available_fonts:
        print(font)
    selected_font = input("Choose a font: ")
    return selected_font

def choose_color():
    available_colors = ["red", "blue", "green", "yellow"]
    print("Available colors:", available_colors)
    selected_color = input("Choose a color: ")
    return selected_color

def choose_symbol():
    symbol = input("Enter a character to use for ASCII art: ")
    return symbol

def format_ascii_art(art, symbol):
    return art.replace('#', symbol)

def save_to_file(ascii_art):
    filename = input("Enter the filename to save the ASCII art: ")
    with open(filename, "w") as file:
        file.write(ascii_art)

def main():
    user_input = get_user_input()
    selected_font = choose_font()
    selected_color = choose_color()
    symbol = choose_symbol()

    ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
    colored_art = colored(ascii_art, color=selected_color)
    formatted_art = format_ascii_art(colored_art, symbol)

    print(formatted_art)
    save_option = input("Do you want to save this ASCII art to a file? (yes/no): ")
    if save_option.lower() == "yes":
        save_to_file(formatted_art)

if __name__ == "__main__":
    main()
