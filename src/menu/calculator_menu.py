from src.classes.input_handling import InputProcessor

class CalculatorMenu:
    def __init__(self, calculator_class):
        self.calculator = calculator_class()

    def calc_memory(self):
        if hasattr(self.calculator, "show_history"):
            self.calculator.show_history()
        else:
            print("This calculator doesn't support history")
            

    def main_menu(self):
        while True:
            print("Main Menu:")
            print("1. Settings Menu")
            print("2. Calculator")
            print("3. View History")
            print("4. Exit")

            option = InputProcessor.get_integer_input("Choose an option (1, 2, 3, or 4): ")

            if option == 1:
                self.settings_menu()
            elif option == 2:
                self.calculator.run()
            elif option == 3:
                self.calc_memory()
            elif option == 4:
                break
