from core.lab_2.lab_2 import HistoryCalculator
from utils.input_handling import get_string_input

class CalculatorMenu:
    def __init__(self, calculator_class):
        self.calculator = calculator_class()

    def calc_memory(self):
        if isinstance(self.calculator, HistoryCalculator):
            self.calculator.show_history()
        else:
            print("Memory feature is not available for the basic Calculator.")

    def main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Settings Menu")
            print("2. Calculator")
            print("3. View History")
            print("4. Exit")

            option = get_string_input("Choose an option (1, 2, 3, or 4): ")

            if option == '1':
                self.settings_menu()
            elif option == '2':
                self.calculator.run()
            elif option == '3':
                self.calc_memory()
            elif option == '4':
                break
