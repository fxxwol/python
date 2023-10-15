# input_handling.py

def get_float_input(prompt, error_message="Введіть правильне число: "):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(error_message)

def get_integer_input(prompt, error_message="Введіть ціле число: "):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(error_message)

def get_string_input(prompt):
    return input(prompt)
