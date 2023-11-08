import unittest
from unittest.mock import patch
import sys
from importlib.machinery import SourceFileLoader

sys.path.append(r"D:\Лаби\3 курс\Лаби\Пітон\python")

lab2_module = SourceFileLoader(
    "calculator",
    r"D:\Лаби\3 курс\Лаби\Пітон\python\lab_2\lab_2.py",
).load_module()

class CalculatorTests(unittest.TestCase):
    def setUp(self):
        self.calculator = lab2_module.HistoryCalculator()

    @patch("builtins.input", side_effect=[5, 3, "+"])
    def test_addition(self, mock_input):
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 8)

    @patch("builtins.input", side_effect=[5, 3, "-"])
    def test_subtraction(self, mock_input):
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 2)

    @patch("builtins.input", side_effect=[5, 3, "*"])
    def test_multiplication(self, mock_input):
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 15)

    @patch("builtins.input", side_effect=[6, 2, "/"])
    def test_division(self, mock_input):
        self.calculator.calculate()
        self.assertEqual(self.calculator.result, 3)

    @patch("builtins.input", side_effect=[6, 0, "/"])
    @patch("builtins.print")
    def test_division_by_zero(self, mock_print, mock_input):
        self.calculator.calculate()
        mock_print.assert_called_with("Division by zero is not allowed.")   

    @patch("builtins.input", side_effect=[5, 7, "+"])
    def test_add_to_history(self, mock_input):
        self.calculator.calculate()
        self.assertEqual(self.calculator.history, ["5.0 + 7.0 = 12.0"])


if __name__ == "__main__":
    unittest.main()