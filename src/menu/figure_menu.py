from src.classes.input_handling import InputProcessor
from src.classes.ascii_art import ArtSettings
from src.core.lab_5.figure import *

class FigureMenu:
    def __init__(self):
        self.is_figure_available = False
        self.is_3d_representation_available = False
        self.figure = None

    def get_character_input(self):
        while True:
            character = ArtSettings.choose_symbol()
            if Figure3D.is_appropriate_character(character) is False:
                print("You should have entered one character!")
            else:
                return character

    def choose_color(self):
        return ArtSettings.choose_color()

    def get_width(self):
        return ArtSettings.choose_max_width()

    def get_scale_input(self):
        while True:
            try:
                scale = InputProcessor.get_float_input("Enter a scale for the figure: ")
                if scale <= 0:
                    print("You should have entered a scale greater than 0!")
                else:
                    return scale
            except ValueError:
                print("You should have entered a float number!")

    def create_cube(self):
        character = self.get_character_input()
        color_position = self.choose_color()
        width = self.get_width()
        scale = self.get_scale_input()
        try:
            self.figure = Cube(width, character, color_position)
            self.is_figure_available = True
            representation_3d = self.figure.get_3d_representation(scale=scale)
            print(representation_3d)
            self.is_3d_representation_available = True
        except ValueError as e:
            print(e)
            self.is_figure_available = False

    def display_2d_representation(self):
        if self.is_figure_available:
            representation_2d = self.figure.get_2d_representation()
            [print(item) for item in representation_2d]
        else:
            print("There is no figure available!")

    def save_3d_representation(self):
        if self.is_3d_representation_available:
            ArtSettings.save_to_file(self.figure.get_3d_representation())
        else:
            print("There is no figure available!")

    def run(self):
        while True:
            print("1 - Create a cube")
            print("2 - Display 2D")
            print("3 - Save 3D")
            print("0 - Exit")
            option = input("Enter an option: ")

            match option:
                case "1":
                    self.create_cube()
                case "2":
                    self.display_2d_representation()
                case "3":
                    self.save_3d_representation()
                case "0":
                    return
                case _:
                    print("Invalid option!")

