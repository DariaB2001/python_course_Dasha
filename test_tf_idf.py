import unittest
from tf_idf import TF_IDF


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tf_idf = TF_IDF('/home/dasha/PycharmProjects/python_course_Dasha/idf.json', 'texts_collection.txt')

    def test_not_zero(self):  # проверяем, что слова встречаются в текстах НЕ 0 раз, чтобы не было ошибки деления на 0
        with open('texts_collection.txt', 'r') as f2:
            texts = f2.read()  # читаем из файла коллекцию текстов; каждый следующий текст начинается с новой строки
            texts_list = texts.split('\n')  # создаём список из текстов
            words_list = []  # список слов всех текстов
            list_of_lists = []  # список, состоящий из списков слов для каждого текста
            for text in texts_list:  # в цикле перебираем все тексты коллекции
                words_of_text_raw = text.split()
                words_of_text = []  # список слов данного текста
                for word_raw in words_of_text_raw:
                    words_list.append(word_raw.strip('.,!?(){}[]«»').lower())
                    words_of_text.append(word_raw.strip('.,!?(){}[]«»').lower())
                list_of_lists.append(words_of_text)
            for word in words_list:  # перебираем все слова корпуса текстов
                n = 0
                for list_of_words in list_of_lists:
                    if word in list_of_words:
                        n += 1
                self.assertNotEqual(n, 0)

    def test_not_empty(self):  # проверяем, что файл непустой
        idf_dict = self.tf_idf.get_load('idf.json')
        self.assertGreater(len(idf_dict), 0)


if __name__ == '__main__':
    unittest.main()
