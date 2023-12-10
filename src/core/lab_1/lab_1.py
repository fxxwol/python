from classes.calculator import Calculator
from menu.calculator_menu import CalculatorMenu

def main():
    menu = CalculatorMenu(Calculator)
    menu.main_menu()

if __name__ == "__main__":
    main()