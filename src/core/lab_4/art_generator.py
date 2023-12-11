import os


class ArtGenerator:
    def __init__(self, ascii_dict, max_width, alignment):
        self.ascii_dict = ascii_dict
        self.max_width = max_width
        self.alignment = alignment

    def get_valid_text(self):
        while True:
            text = input("Enter a word or phrase: ")
            if all(c in self.ascii_dict or c == " " for c in text):
                return text
            else:
                raise ValueError(
                    "Error. The input contains invalid characters. Please enter a valid phrase."
                )

    def print_ascii_art(self, text):
        output_lines = [""] * 6

        for symbol in text:
            if symbol == " ":
                for i in range(6):
                    output_lines[i] += " "
            elif symbol in self.ascii_dict:
                symbol_lines = self.ascii_dict[symbol]
                for i in range(6):
                    output_lines[i] += symbol_lines[i]

        if len(output_lines[0]) > self.max_width:
            raise ValueError("Error. Maximum width is too small for the input phrase.")

        if self.alignment == "center":
            output_lines = [line.center(self.max_width) for line in output_lines]
        elif self.alignment == "right":
            output_lines = [line.rjust(self.max_width) for line in output_lines]

        for line in output_lines:
            print(line)
        return output_lines
