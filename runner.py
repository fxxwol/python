from src.utils.input_handling import get_integer_input
import src.core.lab_1.lab_1 as lab_1
import src.core.lab_2.lab_2 as lab_2
import src.core.lab_3.lab_3 as lab_3
import src.core.lab_4.lab_4 as lab_4
import src.core.lab_5.lab_5 as lab_5
import src.core.lab_6.lab_6 as lab_6
import src.core.lab_7.lab_7 as lab_7
import src.core.lab_8.lab_8 as lab_8

if __name__ == "__main__":

    def choose_lab():
        while True:
            lab_number = get_integer_input("Оберіть номер лабораторної (1-8): ")
            if 1 <= lab_number <= 8:
                return lab_number
            else:
                print("Введений номер не відповідає жодній лабораторній роботі (1-8)")

    lab_number = choose_lab()

    while True:
        match lab_number:
            case 1:
                lab_1.main()
                break
            case 2:
                lab_2.main()
                break
            case 3:
                lab_3.main()
                break
            case 4:
                lab_4.main()
                break
            case 5:
                lab_5.main()
                break
            case 6:
                lab_6.main()
                break
            case 7:
                lab_7.main()
                break
            case 8:
                lab_8.main()
                break
            case 0:
                break
