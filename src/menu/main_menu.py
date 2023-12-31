from src.classes.input_handling import InputProcessor
import src.core.lab_1.lab_1 as lab_1
import src.core.lab_2.lab_2 as lab_2
import src.core.lab_3.lab_3 as lab_3
import src.core.lab_4.lab_4 as lab_4
import src.core.lab_5.lab_5 as lab_5
import src.core.lab_6.lab_6 as lab_6
import src.core.lab_7.lab_7 as lab_7
import src.core.lab_8.lab_8 as lab_8


class MainMenu:
    def choose_lab(self):
        while True:
            lab_number = InputProcessor.get_integer_input("Choose a lab number (1-8, 0 to exit): ")
            if 0 <= lab_number <= 8:
                return lab_number
            else:
                print(
                    "Invalid lab number. Please enter a number between 1 and 8 or 0 to exit."
                )

    def run_lab(self, lab_number):
        labs = [None, lab_1, lab_2, lab_3, lab_4, lab_5, lab_6, lab_7, lab_8]

        if 1 <= lab_number <= 8:
            labs[lab_number].main()

    def run(self):
        while True:
            lab_number = self.choose_lab()

            if lab_number == 0:
                break

            self.run_lab(lab_number)
