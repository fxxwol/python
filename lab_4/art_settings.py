class Settings:
    def __init__(self, max_width, alignment):
        self.max_width = max_width
        self.alignment = alignment

    def get_max_width(self):
        return self.max_width

    def get_alignment(self):
        return self.alignment