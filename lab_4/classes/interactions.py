class UserInteraction:
    @staticmethod
    def select_color():
        color_choice = input("Select text color (white, gray): ").lower()
        if color_choice in ['white', 'gray']:
            return color_choice
        else:
            return None
