from classes.calculator import Calculator
from menu.calculator_menu import CalculatorMenu


class HistoryCalculator(Calculator):
    def __init__(self):
        """
        Initialize a HistoryCalculator object as a subclass of Calculator, with an additional history attribute.
        """
        super().__init__()
        self.history = []

    def calculate(self):
        """
        Perform a calculation, store the full operation and result in the history.
        """
        num1, num2 = self.input_numbers()
        operator = self.input_operator()

        if num1 is not None and num2 is not None and operator is not None:
            try:
                result = None

                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2 == 0:
                        print("Division by zero is not allowed.")
                        return
                    result = num1 / num2
                elif operator == "^":
                    result = num1**num2
                elif operator == "√":
                    result = num1**0.5
                elif operator == "%":
                    result = num1 % num2

                if result is not None:
                    full_operation = f"{num1} {operator} {num2} = {result}"
                    self.history.append(full_operation)

                print("Result:", result)
                self.result = result
            except Exception as e:
                print("Error during calculation:", str(e))

    def show_history(self):
        """
        Display the history of calculations, including the full operations.
        """
        print("Calculation history:")
        for i, operation in enumerate(self.history, 1):
            print(f"{i}: {operation}")


def main():
    menu = CalculatorMenu(HistoryCalculator)
    menu.main_menu()


if __name__ == "__main__":
    main()