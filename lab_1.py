# memory = None

# while True:
#     num1 = float(input("Введіть перше число: "))

#     num2 = float(input("Введіть друге число: "))

#     while True:
#         operator = input("Введіть оператор (+, -, *, /, ^ для піднесення до степеня, √ для квадратного кореня, % для залишку від ділення): ")

#         if operator not in ['+', '-', '*', '/', '^', '√', '%']:
#             print("Невірний оператор. Будь ласка, введіть один із +, -, *, /, ^, √, %.")
#         else:
#             if operator == '+':
#                 result = num1 + num2
#             elif operator == '-':
#                 result = num1 - num2
#             elif operator == '*':
#                 result = num1 * num2
#             elif operator == '/':
#                 if num2 == 0:
#                     print("Помилка: Ділення на нуль.")
#                 else:
#                     result = num1 / num2
#             elif operator == '^':
#                 result = num1 ** num2
#             elif operator == '√':
#                 result = num1 ** 0.5 
#             elif operator == '%':
#                 result = num1 % num2

#             print(f"Результат: {num1} {operator} {num2} = {result}")
            
#             save_to_memory = input("Зберегти результат в пам'яті? (Так/Ні): ")
#             if save_to_memory.lower() == 'так':
#                 memory = result
#                 break

#     another_calculation = input("Виконати ще одне обчислення? (Так/Ні): ")
#     if another_calculation.lower() != 'так':
#         break

# if memory is not None:
#     print(f"Значення в пам'яті: {memory}")

# Ініціалізуємо список для зберігання історії обчислень
calculation_history = []

while True:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    
    while True:
        operator = input("Введіть оператор (+, -, *, /, ^ для піднесення до степеня, √ для квадратного кореня, % для залишку від ділення): ")
        
        if operator not in ['+', '-', '*', '/', '^', '√', '%']:
            print("Невірний оператор. Будь ласка, введіть один із +, -, *, /, ^, √, %.")
        else:
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

            # Записуємо обчислення в історію
            calculation_history.append((num1, operator, num2, result))

            print(f"Результат: {num1} {operator} {num2} = {result}")
            break
    another_calculation = input("Виконати ще одне обчислення? (Так/Ні): ")

    if another_calculation.lower() != 'так':
        print("Історія обчислень:")
        for entry in calculation_history:
            num1, operator, num2, result = entry
            print(f"{num1} {operator} {num2} = {result}")
        break
# Виводимо результат з пам'яті, якщо він бу



# Завдання 9: Історія обчислень
# Створіть журнал, який зберігає історію попередніх обчислень, включаючи вираз і результат. Дозвольте користувачам переглядати історію своїх обчислень.
# Завдання 10: Налаштування користувача
# Надайте користувачам можливість налаштувати поведінку калькулятора, таку як зміну кількості десяткових розрядів, які відображаються, або налаштування функцій пам'яті.