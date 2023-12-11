import pyfiglet
from termcolor import colored
from src.menu.art_menu import ArtMenu
from src.menu.ascii_art_menu import AsciiArtMenu


def main():
    ascii_art_menu = AsciiArtMenu()
    ascii_art_menu.run()


if __name__ == "__main__":
    main()
