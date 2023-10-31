import os

class ArtGenerator:
    def __init__(self, ascii_dict, settings):
        self.ascii_dict = ascii_dict
        self.settings = settings

    def get_valid_text(self):
        while True:
            text = input("Enter a word or phrase: ")
            if all(c in self.ascii_dict or c == ' ' for c in text):
                return text
            else:
                print("Error. The input contains invalid characters. Please enter a valid phrase.")

    def print_ascii_art(self, text, color):
        output_lines = [""] * 6

        for symbol in text:
            if symbol == ' ':
                for i in range(6):
                    output_lines[i] += ' '
            elif symbol in self.ascii_dict:
                symbol_lines = self.ascii_dict[symbol]
                for i in range(6):
                    output_lines[i] += symbol_lines[i]

        if len(output_lines[0]) > self.settings.get_max_width():
            raise ValueError("Error. Maximum width is too small for the input phrase.")

        if self.settings.get_alignment() == 'center':
            output_lines = [line.center(self.settings.get_max_width()) for line in output_lines]
        elif self.settings.get_alignment() == 'right':
            output_lines = [line.rjust(self.settings.get_max_width()) for line in output_lines]

        colored_output_lines = [self.apply_color(line, color) for line in output_lines]

        for line in colored_output_lines:
            print(line)
        return output_lines

    def apply_color(self, text, color):
        color_codes = {'white': '\u001b[97m', 'gray': '\u001b[90m'}
        reset_color = '\u001b[0m'
        return color_codes[color] + text + reset_color
        
    def save_to_text_file(self, output_lines, output_file_name):
        result_folder = "result"
        file_path = os.path.join(result_folder, output_file_name)
        with open(file_path, 'w') as file:
            for line in output_lines:
                file.write(line + '\n')