# Выполнила Красильникова Татьяна Дмитриевна. Группа 44-22-116 . Вариант 6


import unittest
from functions import convert_number, convert_numbers


class TestConvertNumber(unittest.TestCase):
    def test_less_0_2(self):
        """
        тестируем первое условие -- меньше или равен 0.
        """
        result = convert_number("1")
        self.assertEqual(result, "<передано число не из области определения>")

    def test_zero(self):
        """
        тестируем второе условие -- больше 0.
        """
        result = convert_number(0)
        self.assertEqual(result, 1.0)

if __name__ == "__main__":
    unittest.main()
