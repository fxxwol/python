from src.classes.input_handling import InputProcessor


class Calculator:
    """
    The `Calculator` class provides basic arithmetic operations based on user input.

    Attributes:
    - `result`: Holds the result of the latest calculation.

    Methods:
    - `__init__(self)`: Initializes a Calculator object with a `result` attribute.
    - `input_numbers(self) -> tuple`: Prompts the user to input two numbers and returns them as a tuple.
    - `input_operator(self) -> str`: Prompts the user to input an operator and returns it.
    - `calculate(self)`: Performs a calculation based on user input and displays the result.
    - `run(self)`: Runs the calculator, allowing the user to perform calculations repeatedly.

    Usage example:

    ```python
    calculator = Calculator()
    calculator.run()
    ```

    Note: This class relies on the `InputProcessor` class for user input handling.
    """

    def __init__(self):
        """
        Initializes a Calculator object with a result attribute.
        """
        self.result = None

    def input_numbers(self) -> tuple:
        """
        Prompts the user to input two numbers and returns them as a tuple.

        Returns:
        tuple: A tuple containing two numbers entered by the user.
        None: If there is an error in user input.
        """
        try:
            num1 = InputProcessor.get_float_input("Enter the first number: ")
            num2 = InputProcessor.get_float_input("Enter the second number: ")
            return num1, num2
        except ValueError:
            print("Invalid input for numbers.")
            return None

    def input_operator(self) -> str:
        """
        Prompts the user to input an operator and returns it.

        Returns:
        str: The operator entered by the user.
        None: If there is an error in user input.
        """
        operator = InputProcessor.get_string_input(
            "Enter operator (+, -, *, /, ^, √, %): "
        )
        if operator not in ["+", "-", "*", "/", "^", "√", "%"]:
            print("Invalid operator.")
            return None
        return operator

    def calculate(self):
        """
        Performs a calculation based on user input and displays the result.
        """
        num1, num2 = self.input_numbers()
        operator = self.input_operator()

        if num1 is not None and num2 is not None and operator is not None:
            try:
                if operator == "+":
                    self.result = num1 + num2
                elif operator == "-":
                    self.result = num1 - num2
                elif operator == "*":
                    self.result = num1 * num2
                elif operator == "/":
                    try:
                        self.result = num1 / num2
                    except ZeroDivisionError:
                        print("Division by 0 is not allowed")
                        return
                elif operator == "^":
                    self.result = num1**num2
                elif operator == "√":
                    self.result = num1**0.5
                elif operator == "%":
                    self.result = num1 % num2

                print("Result:", self.result)
            except Exception as e:
                print("Error during calculation:", str(e))

    def run(self):
        """
        Runs the calculator, allowing the user to perform calculations repeatedly.
        """
        while True:
            self.calculate()
            choice = InputProcessor.get_string_input(
                "Do you want to perform another calculation? (Yes/No): "
            )
            if choice.lower() != "yes":
                break
