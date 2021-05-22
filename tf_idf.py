import os
import json
import math


class TF_IDF:

    def __init__(self, idf_file, path, texts_collection):
        if os.path.exists(path):
            self.idf = self.load(idf_file)
        else:
            self.idf = self.count_idf(texts_collection)

    def load(self, idf_file):
        with open(idf_file, 'r') as f1:
            idf_dict = json.load(f1)
        return idf_dict

    def count_idf(self, texts_collection):
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
            for word in words_list:  # перебираем все слова корпуса текстов
                n = 0
                for list_of_words in list_of_lists:
                    if word in list_of_words:
                        n += 1
                idf = math.log10(len(texts_list) / n)
                if word not in idf_dict.keys():
                    idf_dict[word] = idf
        with open('idf.json', 'w') as f3:
            json.dump(idf_dict, f3)
        return idf_dict

    def count_tf(self, text): # функция считает tf для всех слов текста и возвращает словарь вида {слово: его tf}
        tf_dict = {}  # словарь значений tf для данного текста
        words_list_raw = text.split()
        words_list = []
        for word_raw in words_list_raw:
            words_list.append(word_raw.strip('.,!?"(){}[]«»').lower())  # список слов текста
        for word in words_list:
            n = 0  # переменная-счётчик
            for w in words_list:
                if w == word:
                    n += 1
            tf = n / len(words_list)
            if word not in tf_dict.keys():
                tf_dict[word] = tf
        return tf_dict

    def count_tf_idf(self, text):  # функция, принимающая на входе текст от пользователя
        # и возвращающая словарь вида {слово: его TF-IDF}
        tf_idf_dict = {}
        text_tf_dict = self.count_tf(text)  # считаем tf для данного текста
        words_of_text_raw = text.split()
        words_of_text = []
        for word_raw in words_of_text_raw:
            words_of_text.append(word_raw.strip('.,!?"(){}[]«»').lower())  # список слов данного текста,
        # для каждого из которых надо посчитать TF-IDF
        text_idf_dict = {}  # словарь со значениями IDF для данного конкретного текста
        for word in words_of_text:
            if word in self.idf.keys():
                text_idf_dict[word] = self.idf[word]
            else:
                text_idf_dict[word] = 0
        for word in words_of_text:
            tf = text_tf_dict[word]
            idf = text_idf_dict[word]
            tf_idf = tf*idf
            if word not in tf_idf_dict.keys():
                tf_idf_dict[word] = tf_idf
        return tf_idf_dict


if __name__ == '__main__':
    tf_idf = TF_IDF('idf.json', '/home/dasha/PycharmProjects/22.05.2021/idf.json', 'texts_collection.txt')
    print(tf_idf.count_tf_idf('Великолепная «Школа злословия» вернулась в эфир после летних каникул в новом формате.'))
