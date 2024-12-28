import unittest 
import calculator

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        string = '3+5'
        result = 8

        self.assertEqual(calculator.run_calculator(string), result)

    def test_subtract_two_numbers(self):
        string = '6-3'
        result = 3

        self.assertEqual(calculator.run_calculator(string), result)

    def test_multiply_two_numbers(self):
        string = '6x3'
        result = 18

        self.assertEqual(calculator.run_calculator(string), result)

    def test_divide_two_numbers(self):
        string = '6/3'
        result = 2

        self.assertEqual(calculator.run_calculator(string), result)

if __name__ == '__main__':
    unittest.main()