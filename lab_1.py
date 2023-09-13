calculation_history = []
decimal_places = 2
memory_option = 'calculation'

def settings_menu():
    while True:
        print("Меню налаштувань:")
        print("1. Змінити кількість десяткових розрядів")
        print("2. Налаштування пам'яті")
        print("3. Вихід з меню налаштувань")
        
        setting_option = input("Виберіть опцію: ")
        
        if setting_option == '1':
            global decimal_places
            decimal_places = int(input("Введіть нову кількість десяткових розрядів: "))
        elif setting_option == '2':
            print("Функція пам'яті:")
            print("1. Виводити історію результатів")
            print("2. Виводити історію обчислень")
            option = input("Виберіть опцію (1 або 2): ")
            if option == '1':
                global memory_option
                memory_option = 'results'
            elif option == '2':
                memory_option = 'calculation'
        elif setting_option == '3':
            break

def calc_memory(history):
    if len(history) != 0:
            print("Історія обчислень:")
            for entry in calculation_history:
                num1, operator, num2, result = entry
                if memory_option == 'calculation':
                    print(f"{num1} {operator} {num2} = {result:.{decimal_places}f}")
                else:
                    print(f"{result:.{decimal_places}}")
    else:
        print("Пам'ять порожня.")


while True:
    print("Головне меню:")
    print("1. Викликати меню налаштувань")
    print("2. Обчислення")
    print("3. Переглянути історію")
    print("4. Вихід")
    
    option = input("Виберіть опцію (1, 2, 3 або 4): ")
    
    if option == '1':
        settings_menu()
    elif option == '2':
        while True:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            
            while True:
                while True:
                    operator = input("Введіть оператор (+, -, *, /, ^ для піднесення до степеня, √ для квадратного кореня, % для залишку від ділення): ")
                    
                    if operator not in ['+', '-', '*', '/', '^', '√', '%']:
                        print("Невірний оператор. Будь ласка, введіть один із +, -, *, /, ^, √, %.")
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
                        print("Помилка: Ділення на нуль.")
                    else:
                        result = num1 / num2
                elif operator == '^':
                    result = num1 ** num2
                elif operator == '√':
                    result = num1 ** 0.5 
                elif operator == '%':
                    result = num1 % num2
                
                calculation_history.append((num1, operator, num2, result))
                
                print(f"Результат: {num1} {operator} {num2} = {result:.{decimal_places}f}")
                
                another_calculation = input("Виконати ще одне обчислення? (Так/Ні): ")
                if another_calculation.lower() != 'так':
                    break
                else:
                    num1 = float(input("Введіть перше число: "))
                    num2 = float(input("Введіть друге число: "))
            break
    elif option == '3':
        calc_memory(calculation_history)
    elif option == '4':
        break
