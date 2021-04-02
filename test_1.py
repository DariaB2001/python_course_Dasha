import unittest


def concatenation(str1, str2):  # функция, конкатенирующая 2 строки
    new_str = str1 + str2
    return new_str


def square(number):  # функция, возводящая заданное число в квадрат
    square = number**2
    return square


def multiply(number):  # функция, которая умножает заданное число на 10
    new_number = int(number)*10
    return new_number


def delete_a(word):  # функция, удаляющая из заданного слова все буквы а
    list_of_letters = list(word)
    new_list_of_letters = []
    for letter in list_of_letters:
        if letter != 'a':
            new_list_of_letters.append(letter)
    new_word = ''.join(new_list_of_letters)
    return new_word


class MyTestCase(unittest.TestCase):
    def test_lengths1(self):  # проводим проверку assertGreater
        str1 = 's1'
        str2 = 's2'
        str3 = concatenation(str1, str2)
        self.assertGreater(len(str3), len(str1))  # проверяем, что длина новой строки
        # больше длины каждой из исходных строк
        self.assertGreater(len(str3), len(str2))

    def test_lengths2(self):  # проводим проверку assertLess
        str1 = 's1'
        str2 = 's2'
        str3 = concatenation(str1, str2)
        self.assertLess(len(str2), len(str3))  # проверяем, что каждая из длин исходных строк меньше длины новой строки
        self.assertLess(len(str1), len(str3))

    def test_true(self):  # проводим проверку assertTrue
        str1 = 's1'
        str2 = 's2'
        str3 = concatenation(str1, str2)
        self.assertTrue(len(str3) > len(str2))  # проверяем: длина новой строки больше
        # длины исходной строки - это правда?
        self.assertTrue(len(str3) > len(str1))

    def test_false(self):  # проводим проверку assertFalse
        str1 = 's1'
        str2 = 's2'
        str3 = concatenation(str1, str2)
        self.assertFalse(len(str3) < len(str2))  # проверяем: длина новой строки меньше
        # длины исходной строки - это ложь?
        self.assertFalse(len(str3) < len(str1))

    def test_equal(self):  # проводим проверку assertCountEqual
        n = 162
        s = square(n)
        self.assertCountEqual(str(s), str(n * n))

    def test_in(self):  # проводим проверку assertIn
        new_number = multiply(150)
        self.assertIn(str(0), str(new_number))

    def test_not_in(self):  # проводим проверку assertNotIn
        word = delete_a('aajjnnanjnja')
        self.assertNotIn('a', word)


if __name__ == '__main__':
    unittest.main()
