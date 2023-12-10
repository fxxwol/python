from utils.input_handling import get_integer_input
import core

if __name__ == "__main__":

    def choose_lab():
        while True:
            lab_number = get_integer_input("Оберіть номер лабораторної (1-8): ")
            if 1 <= lab_number <= 7:
                return lab_number
            else:
                print("Введений номер не відповідає жодній лабораторній роботі (1-8)")

    lab_number = choose_lab()

    while True:
        match lab_number:
            case 1:
                core.lab_1.lab_1.main()
            case 2:
                core.lab_2.lab_2.main()
            case 3:
                core.lab_3.lab_3.main()
            case 4:
                core.lab_4.lab_4.main()
            case 5:
                core.lab_5.lab_5.main()
            case 6:
                core.lab_6.lab_6.main()
            case 7:
                core.lab_7.lab_7.main()
            case 8:
                core.lab_8.lab_8.main()
            case 0:
                break
