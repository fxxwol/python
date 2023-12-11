from src.core.lab_5.figure import Cube
from src.menu.art_menu import ArtMenu


class FigureMenu(ArtMenu):
    def run(self):
        is_figure_available: bool = False
        is_3d_representation_available = False

        colors = ["red", "blue", "green", "yellow"]

        while True:
            options = {
                "1": "Create a cube",
                "2": "Display 2D",
                "3": "Save 3D",
                "0": "Exit",
            }
            option = self.get_option(options)

            if option == "1":
                character = self.get_character_input()
                print("There are such colors available:")
                self.display_options({str(i): color for i, color in enumerate(colors)})
                color = self.get_color_position_input(colors)
                length = self.get_length_input()
                scale = self.get_scale_input()

                try:
                    figure = Cube(length, character, color)
                    is_figure_available = True
                    representation_3d = figure.get_3d_representation(scale=scale)
                    print(representation_3d)
                    is_3d_representation_available = True
                except ValueError as e:
                    print(e)
                    is_figure_available = False

            elif option == "2":
                if is_figure_available:
                    representation_2d = figure.get_2d_representation()
                    [print(item) for item in representation_2d]
                else:
                    print("There is no figure available!")

            elif option == "3":
                if is_3d_representation_available:
                    file_path = self.choose_file_path()
                    try:
                        with open(file_path, "w") as file:
                            file.write(representation_3d)
                        print(f"3D representation saved to {file_path}")
                    except PermissionError:
                        print("You do not have permission to write to the file!")
                    except FileNotFoundError:
                        print("The file does not exist!")
                else:
                    print("There is no figure available!")

            elif option == "0":
                break

            else:
                print("Invalid option!")
