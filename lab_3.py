import pyfiglet
from termcolor import colored
from utils.input_handling import get_string_input, get_integer_input
# Function to get user input
def get_user_input():
    user_input = get_string_input("Enter a word or phrase: ")
    return user_input

# Function to choose a font for ASCII art
def choose_font():
    available_fonts = pyfiglet.FigletFont.getFonts()
    print("Available fonts:")
    for font in available_fonts:
        print(font)
    selected_font = get_string_input("Choose a font: ")
    return selected_font

# Function to choose a color for ASCII art
def choose_color():
    available_colors = ["red", "blue", "green", "yellow"]
    print("Available colors:", available_colors)
    selected_color = get_string_input("Choose a color: ")
    return selected_color

# Function to choose a symbol for customizing ASCII art
def choose_symbol():
    symbol = get_string_input("Enter a character to use for ASCII art: ")
    return symbol

# Function to format ASCII art by replacing '#' with a custom symbol
def format_ascii_art(art, symbol):
    return art.replace('#', symbol)

# Function to resize ASCII art to a specified width and height
def resize_ascii_art(ascii_art, width, height):
    # Split the ASCII art into lines
    lines = ascii_art.split('\n')

    # Resize the ASCII art to the specified height
    while len(lines) < height:
        lines.append(' ' * len(lines[0]))

    # Resize each line to the specified width
    for i in range(len(lines)):
        lines[i] = lines[i].ljust(width)[:width]

    return '\n'.join(lines)

# Function to save ASCII art to a file
def save_to_file(ascii_art):
    filename = get_string_input("Enter the filename to save the ASCII art: ")
    with open(filename, "w") as file:
        file.write(ascii_art)

# Main function
def main():
    user_input = get_user_input()
    selected_font = choose_font()
    selected_color = choose_color()
    symbol = choose_symbol()

    # Generate ASCII art using pyfiglet and color it
    ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
    colored_art = colored(ascii_art, color=selected_color)
    
    # Format the ASCII art with the chosen symbol
    formatted_art = format_ascii_art(colored_art, symbol)

    print(formatted_art)

    # Get user input for desired width and height
    width = get_integer_input("Enter the desired width (number of columns): ")
    height = get_integer_input("Enter the desired height (number of rows): ")
    
    # Resize the ASCII art
    resized_art = resize_ascii_art(formatted_art, width, height)

    print(resized_art)

    # Ask the user if they want to save the ASCII art to a file
    save_option = get_string_input("Do you want to save this ASCII art to a file? (yes/no): ")
    if save_option.lower() == "yes":
        save_to_file(resized_art)

if __name__ == "__main__":
    main()
