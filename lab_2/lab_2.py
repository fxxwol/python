from utils.input_handling import get_string_input, get_float_input

class Calculator:
    def __init__(self):
        """
        Initialize a Calculator object with a result attribute.
        """
        self.result = None

    def input_numbers(self):
        """
        Prompt the user to input two numbers and return them as a tuple.
        """
        try:
            num1 = get_float_input("Enter the first number: ")
            num2 = get_float_input("Enter the second number: ")
            return num1, num2
        except ValueError:
            print("Invalid input for numbers.")
            return None

    def input_operator(self):
        """
        Prompt the user to input an operator and return it.
        """
        operator = get_string_input("Enter operator (+, -, *, /, ^, √, %): ")
        if operator not in ['+', '-', '*', '/', '^', '√', '%']:
            print("Invalid operator.")
            return None
        return operator

    def calculate(self):
        """
        Perform a calculation based on user input and display the result.
        """
        num1, num2 = self.input_numbers()
        operator = self.input_operator()

        if num1 is not None and num2 is not None and operator is not None:
            try:
                if operator == '+':
                    self.result = num1 + num2
                elif operator == '-':
                    self.result = num1 - num2
                elif operator == '*':
                    self.result = num1 * num2
                elif operator == '/':
                    try:
                        self.result = num1 / num2
                    except ZeroDivisionError:
                        print("Division by 0 is not allowed")
                        return
                elif operator == '^':
                    self.result = num1 ** num2
                elif operator == '√':
                    self.result = num1 ** 0.5
                elif operator == '%':
                    self.result = num1 % num2

                print("Result:", self.result)
            except Exception as e:
                print("Error during calculation:", str(e))

    def run(self):
        """
        Run the calculator, allowing the user to perform calculations repeatedly.
        """
        while True:
            self.calculate()
            choice = get_string_input("Do you want to perform another calculation? (Yes/No): ")
            if choice.lower() != 'yes':
                break


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

                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 == 0:
                        print("Division by zero is not allowed.")
                        return
                    result = num1 / num2
                elif operator == '^':
                    result = num1 ** num2
                elif operator == '√':
                    result = num1 ** 0.5
                elif operator == '%':
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
    calc = HistoryCalculator()
    calc.run()
    calc.show_history()
