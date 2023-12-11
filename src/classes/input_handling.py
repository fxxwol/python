class InputProcessor:
    """
    The `InputProcessor` class provides methods for obtaining user input with error handling.

    Methods:
    - `get_float_input(prompt, error_message="Enter float value: ") -> float`: Obtains a float input from the user.
    - `get_integer_input(prompt, error_message="Enter integer value: ") -> int`: Obtains an integer input from the user.
    - `get_string_input(prompt) -> str`: Obtains a string input from the user.
    - `get_yes_no_input(prompt) -> str`: Obtains a yes/no input from the user.

    Usage example:

    ```python
    input_processor = InputProcessor()
    float_value = input_processor.get_float_input("Enter a float value: ")
    integer_value = input_processor.get_integer_input("Enter an integer value: ")
    string_value = input_processor.get_string_input("Enter a string: ")
    yes_no_choice = input_processor.get_yes_no_input("Do you want to proceed? (yes/no): ")
    ```

    Note: This class is designed to handle float, integer, string, and yes/no inputs with appropriate error messages.
    """

    @staticmethod
    def get_float_input(prompt, error_message="Enter float value: ") -> float:
        """
        Obtains a float input from the user with error handling.

        Parameters:
        - `prompt` (str): The prompt message displayed to the user.
        - `error_message` (str): The error message displayed if the input is not a float.

        Returns:
        float: The float value entered by the user.
        """
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print(error_message)

    @staticmethod
    def get_integer_input(prompt, error_message="Enter integer value: ") -> int:
        """
        Obtains an integer input from the user with error handling.

        Parameters:
        - `prompt` (str): The prompt message displayed to the user.
        - `error_message` (str): The error message displayed if the input is not an integer.

        Returns:
        int: The integer value entered by the user.
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print(error_message)

    @staticmethod
    def get_string_input(prompt) -> str:
        """
        Obtains a string input from the user.

        Parameters:
        - `prompt` (str): The prompt message displayed to the user.

        Returns:
        str: The string value entered by the user.
        """
        return input(prompt)

    @staticmethod
    def get_yes_no_input(prompt) -> str:
        """
        Obtains a yes/no input from the user with error handling.

        Parameters:
        - `prompt` (str): The prompt message displayed to the user.

        Returns:
        str: The user's choice ('yes' or 'no').
        """
        while True:
            choice = input(prompt).strip().lower()
            if choice in ["yes", "no"]:
                return choice
            else:
                print("Error! Please enter 'yes' or 'no'.")
