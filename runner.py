import os
import sys
from utils.input_handling import get_integer_input


def choose_lab():
    while True:
        lab_number = get_integer_input("Оберіть номер лабораторної (1-5): ")
        if 1 <= lab_number <= 5:
            return lab_number
        else:
            print("Введений номер не відповідає жодній лабораторній роботі (1-5)")


lab_number = choose_lab()

current_directory = os.path.dirname(os.path.abspath(__file__))

lab_file_path = os.path.join(
    current_directory, f"lab_{lab_number}", f"lab_{lab_number}.py"
)

if os.path.isfile(lab_file_path):
    with open(lab_file_path, "r", encoding="utf-8") as lab_file:
        exec(lab_file.read())
else:
    print(f"Файл для лабораторної роботи {lab_number} не знайдено.")
