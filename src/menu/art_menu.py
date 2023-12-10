from classes.file_processor import FileProcessor
class ArtMenu:
    @staticmethod
    def get_option():
        while True:
            try:
                option = input("Enter an option: ")
                return option
            except ValueError:
                print("Invalid input. Please enter a valid option.")

    @staticmethod
    def display_options(options):
        for key, value in options.items():
            print(f"{key} - {value}")

    @staticmethod
    def get_color_position_input(colors):
        while True:
            try:
                color = int(input("Enter a number of color: "))
                if color not in range(len(colors)):
                    print("You should have entered a color option which is available!")
                else:
                    return color
            except ValueError:
                print("You should have entered an integer number!")

    @staticmethod
    def get_length_input():
        while True:
            try:
                length = int(input("Enter a length: "))
                if length <= 0:
                    print("You should have entered a length greater than 0!")
                else:
                    return length
            except ValueError:
                print("You should have entered an integer number!")

    @staticmethod
    def get_scale_input():
        while True:
            try:
                scale = float(input("Enter a scale for the figure: "))
                if scale <= 0:
                    print("You should have entered a scale greater than 0!")
                else:
                    return scale
            except ValueError:
                print("You should have entered a float number!")

    @staticmethod
    def save_to_file(file_name, content):
        file_processor = FileProcessor(file_name)
        file_processor.save_to_file(content)