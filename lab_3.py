import pyfiglet

def get_user_input():
    user_input = input("Введіть слово або фразу: ")
    return user_input

def choose_font():
    fonts = ["block", "big", "doom", "banner"]
    print("Доступні шрифти:")
    for i, font in enumerate(fonts, start=1):
        print(f"{i}. {font.capitalize()}")
    
    font_choice = int(input("Оберіть номер шрифту: ")) - 1
    selected_font = fonts[font_choice]
    return selected_font

def choose_text_color():
    print("Доступні кольори:")
    print("1. Червоний")
    print("2. Синій")
    print("3. Зелений")
    print("4. Жовтий")
    
    color_choice = int(input("Оберіть номер кольору: "))
    colors = ["red", "blue", "green", "yellow"]
    selected_color = colors[color_choice - 1]
    return selected_color

def choose_art_size():
    width = int(input("Введіть ширину ASCII-арту: "))
    height = int(input("Введіть висоту ASCII-арту: "))
    return width, height

def choose_art_characters():
    characters = input("Введіть символи для ASCII-арту (за замовчуванням - '#'): ")
    if not characters:
        characters = "#"
    return characters

def preview_ascii_art(ascii_art, text_color):
    print("Попередній перегляд ASCII-арту:")
    print(ascii_art)

def save_to_file(ascii_art):
    file_name = input("Введіть ім'я файлу для збереження ASCII-арту: ")
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файлі {file_name}")

def main():
    user_input = get_user_input()
    selected_font = choose_font()
    selected_color = choose_text_color()
    width, height = choose_art_size()
    characters = choose_art_characters()
    
    ascii_art_generator = pyfiglet.Figlet(font=selected_font)
    ascii_art = ascii_art_generator.renderText(user_input)
    
    # Масштабуємо ASCII-арт
    lines = ascii_art.split("\n")
    scaled_art = ""
    for line in lines:
        for _ in range(height):
            scaled_art += line + "\n"
    
    scaled_art = scaled_art.rstrip()  # Видаляємо зайві символи нового рядка з кінця
    
    preview_ascii_art(scaled_art, selected_color)
    
    save_option = input("Зберегти ASCII-арт у файл? (Так/Ні): ").strip().lower()
    if save_option == "так":
        save_to_file(scaled_art)

if __name__ == "__main__":
    main()
