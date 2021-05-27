import os
import json
import math


class TF_IDF:

    def __init__(self, path, texts_collection):
        if os.path.exists(path):
            self._idf = self._load(path)
        else:
            self._idf = self._count_idf(texts_collection)

    def _load(self, path):
        with open(path, 'r') as f1:
            idf_dict = json.load(f1)
        return idf_dict

    def get_load(self, path):
        return self._load(path)

    def get_idf(self):
        return self._idf

    def _count_idf(self, texts_collection):
        with open(texts_collection, 'r') as f2:
            texts = f2.read()  # читаем из файла коллекцию текстов; каждый следующий текст начинается с новой строки
            idf_dict = {}  # словарь вида {слово: его idf}
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
            for word in set(words_list):  # перебираем все слова корпуса текстов
                n = 0
                for list_of_words in list_of_lists:
                    if word in list_of_words:
                        n += 1
                idf = math.log10(len(texts_list) / n)
                idf_dict[word] = idf
        with open('idf.json', 'w') as f3:
            json.dump(idf_dict, f3)
        return idf_dict

    def _count_tf(self, text): # функция считает tf для всех слов текста и возвращает словарь вида {слово: его tf}
        tf_dict = {}  # словарь значений tf для данного текста
        words_list_raw = text.split()
        words_list = []
        for word_raw in words_list_raw:
            words_list.append(word_raw.strip('.,!?"(){}[]«»').lower())  # список слов текста
        words = list(set(words_list))
        for word in words:
            n = words_list.count(word)
            tf = n / len(words_list)
            tf_dict[word] = tf
        return tf_dict

    def get_count_tf(self, text):
        return self._count_tf(text)

    def count_tf_idf(self, text):  # функция, принимающая на входе текст от пользователя
        # и возвращающая словарь вида {слово: его TF-IDF}
        tf_idf_dict = {}
        text_tf_dict = self._count_tf(text)  # считаем tf для данного текста
        text_idf_dict = {}  # словарь со значениями IDF для данного конкретного текста
        for word in text_tf_dict.keys():
            if word in self._idf.keys():
                text_idf_dict[word] = self._idf[word]
        for word, tf in text_tf_dict.items():
            if word in self._idf.keys():
                tf_idf_dict[word] = tf * self._idf[word]
            else:
                tf_idf_dict[word] = 0
        return tf_idf_dict


if __name__ == '__main__':
    tf_idf = TF_IDF('/home/dasha/PycharmProjects/python_course_Dasha/idf.json', 'texts_collection.txt')
    print(tf_idf.count_tf_idf('Великолепная «Школа злословия» вернулась в эфир после летних каникул в новом формате.'))
