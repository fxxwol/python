from utils.input_handling import get_float_input, get_integer_input, get_string_input

calculation_history = []
decimal_places = 2
memory_option = 'calculation'

def settings_menu():
    while True:
        print("Settings Menu:")
        print("1. Change Decimal Places")
        print("2. Memory Settings")
        print("3. Back to Main Menu")

        setting_option = get_string_input("Choose an option: ")

        if setting_option == '1':
            global decimal_places
            decimal_places = get_integer_input("Enter the number of decimal places: ")
        elif setting_option == '2':
            print("Memory Function:")
            print("1. Show Results History")
            print("2. Show Calculation History")
            option = get_string_input("Choose an option (1 or 2): ")
            if option == '1':
                global memory_option
                memory_option = 'results'
            elif option == '2':
                memory_option = 'calculation'
        elif setting_option == '3':
            break

def calc_memory(history):
    if len(history) != 0:
        print("Calculation History:")
        for entry in calculation_history:
            num1, operator, num2, result = entry
            if memory_option == 'calculation':
                if operator == '√':
                    print(f"{operator} {num1} = {result:.{decimal_places}f}")
                else:
                    print(f"{num1} {operator} {num2} = {result:.{decimal_places}f}")
            else:
                print(f"{result:.{decimal_places}}")
    else:
        print("Memory is empty.")

def main():
    while True:
        print("Main Menu:")
        print("1. Settings Menu")
        print("2. Calculator")
        print("3. View History")
        print("4. Exit")

        option = input("Choose an option (1, 2, 3, or 4): ")

        if option == '1':
            settings_menu()
        elif option == '2':
            while True:
                num1 = get_float_input("Enter the first number: ")
                num2 = get_float_input("Enter the second number: ")
                
                while True:
                    while True:
                        operator = get_string_input("Enter operator (+, -, *, /, ^ for exponentiation, √ for square root, % for modulus): ")
                        
                        if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                            print("Invalid operator. Please enter one of +, -, *, /, ^, √, %.")
                        else:
                            break
                    
                    if operator == '+':
                        result = num1 + num2
                    elif operator == '-':
                        result = num1 - num2
                    elif operator == '*':
                        result = num1 * num2
                    elif operator == '/':
                        if num2 == 0:
                            print("Error: Division by zero.")
                            break
                        else:
                            result = num1 / num2
                    elif operator == '^':
                        result = num1 ** num2
                    elif operator == '√':
                        result = num1 ** 0.5 
                    elif operator == '%':
                        result = num1 % num2
                    
                    calculation_history.append((num1, operator, num2, result))
                    if(operator == '√'):
                        print(f"Result: {operator} {num1} = {result:.{decimal_places}f}")
                    else:
                        print(f"Result: {num1} {operator} {num2} = {result:.{decimal_places}f}")
                    
                    another_calculation = get_string_input("Perform another calculation? (Yes/No): ")
                    if another_calculation.lower() != 'yes':
                        break
                    else:
                        num1 = get_float_input("Enter the first number: ")
                        num2 = get_float_input("Enter the second number: ")
                break
        elif option == '3':
            calc_memory(calculation_history)
        elif option == '4':
            break