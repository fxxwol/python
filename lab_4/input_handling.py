def get_float_input(prompt, error_message="Enter float value: "):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(error_message)


def get_integer_input(prompt, error_message="Enter integer value: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(error_message)


def get_string_input(prompt):
    return input(prompt)
