from utils.input_handling import get_integer_input
import lab_1.lab_1
import lab_2.lab_2
import lab_3.lab_3
import lab_4.lab_4
import lab_5.lab_5
import lab_6.lab_6

if __name__ == "__main__":      
    def choose_lab():
        while True:
            lab_number = get_integer_input("Оберіть номер лабораторної (1-5): ")
            if 1 <= lab_number <= 6:
                return lab_number
            else:
               print("Введений номер не відповідає жодній лабораторній роботі (1-5)")


    lab_number = choose_lab()

    while True:
        match lab_number:
            case 1:
                lab_1.lab_1.main()
            case 2:
                lab_2.lab_2.main()
            case 3:
                lab_3.lab_3.main()
            case 4:
                lab_4.lab_4.main()
            case 5:
                lab_5.lab_5.main()
            case 6:
                lab_6.lab_6.main()
            case 0:
                break
