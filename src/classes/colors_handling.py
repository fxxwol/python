import colorama
from colorama import Fore


class ColorProcessor:
    def __init__(self):
        colorama.init(autoreset=True)
        self.colors = dict(enumerate(sorted(Fore.__dict__.keys())))

    def display_colors(self) -> None:
        for i in self.colors:
            print(str(i) + ". " + self.colors[i])