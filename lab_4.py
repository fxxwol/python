from utils.input_handling import get_string_input, get_integer_input

user_input = get_string_input("Введіть слово або фразу, яку ви хочете перетворити в ASCII-арт: ")

# Characters set
characters = ["@", "#", "%", "?", "*", "+", ";", ":", ",", "."]

# Set size 
width = get_integer_input("Введіть ширину ASCII-арту (від 1 до 100): ", "Розмір має бути цілим числом в межах вказаних значень.")
height = get_integer_input("Введіть висоту ASCII-арту (від 1 до 100): ", "Розмір має бути цілим числом в межах вказаних значень.")

# Generate art
def generate_ascii_art(user_input, characters, width, height):
    ascii_art = ""
    for i in range(height):
        line = ""
        for char in user_input:
            char_index = ord(char) % len(characters)
            line += characters[char_index] * (width // len(user_input))
        ascii_art += line + "\n"
    return ascii_art

# Displaying art
art = generate_ascii_art(user_input, characters, width, height)
print(f"{user_input} ASCII-арт:")
print(art)

# Save to file
while True:
    choice = get_string_input("Бажаєте зберегти ASCII-арт у файл? (Так/Ні): ").lower()
    if choice == "так":
        filename = get_string_input("Введіть ім'я файлу для збереження ASCII-арту: ")
        try:
            with open(filename, "w") as file:
                file.write(art)
            print(f"ASCII-арт збережено у файлі {filename}")
        except Exception as e:
            print(f"Помилка при збереженні файлу: {e}")
        break
    elif choice == "ні":
        break
    else:
        print("Будь ласка, введіть 'Так' або 'Ні'.")
