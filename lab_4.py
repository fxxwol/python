# Завдання 1: Введення користувача
user_input = input("Введіть слово або фразу, яку ви хочете перетворити в ASCII-арт: ")

# Завдання 2: Набір символів
characters = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Завдання 3: Розміри Art-у
while True:
    try:
        width = int(input("Введіть ширину ASCII-арту (від 1 до 100): "))
        height = int(input("Введіть висоту ASCII-арту (від 1 до 100): "))
        if 1 <= width <= 100 and 1 <= height <= 100:
            break
        else:
            print("Розміри мають бути в межах вказаних значень.")
    except ValueError:
        print("Введіть числа.")

# Завдання 4: Функція генерації Art-у
def generate_ascii_art(user_input, characters, width, height):
    ascii_art = ""
    for i in range(height):
        line = ""
        for char in user_input:
            char_index = ord(char) % len(characters)
            line += characters[char_index] * (width // len(user_input))
        ascii_art += line + "\n"
    return ascii_art

# Завдання 6: Відображення мистецтва
art = generate_ascii_art(user_input, characters, width, height)
print(f"{user_input} ASCII-арт:")
print(art)

# Завдання 7: Збереження у файл
while True:
    choice = input("Бажаєте зберегти ASCII-арт у файл? (Так/Ні): ").lower()
    if choice == "так":
        filename = input("Введіть ім'я файлу для збереження ASCII-арту: ")
        with open(filename, "w") as file:
            file.write(art)
        print(f"ASCII-арт збережено у файлі {filename}")
        break
    elif choice == "ні":
        break
    else:
        print("Будь ласка, введіть 'Так' або 'Ні'.")
