import unittest
import random


class MyTestCase(unittest.TestCase):
    def test_more_than_half(self):
        l = []  # список, содержащий 10 случайных чисел в диапазоне от 0 до 1
        for i in range(10):
            l.append(random.random())
        for num in l:
            with self.subTest(i=num):
                self.assertGreaterEqual(num, 0.5)  # проверяем каждое число списка:
                # оно больше или равно, чем 0.5, или нет?


if __name__ == '__main__':
    unittest.main()
