from src.utils.input_handling import get_integer_input

class CalculatorMenu:
    def __init__(self, calculator_class):
        self.calculator = calculator_class()

    def calc_memory(self):
            self.calculator.show_history()

    def main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Settings Menu")
            print("2. Calculator")
            print("3. View History")
            print("4. Exit")

            option = get_integer_input("Choose an option (1, 2, 3, or 4): ")

            if option == 1:
                self.settings_menu()
            elif option == 2:
                self.calculator.run()
            elif option == 3:
                self.calc_memory()
            elif option == 4:
                break
