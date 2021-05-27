import unittest
from tf_idf import TF_IDF


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tf_idf = TF_IDF('/home/dasha/PycharmProjects/python_course_Dasha/idf.json', 'texts_collection.txt')

    def test_equal(self):  # проверяем, что словари с tf и с tf-idf содержат одинаковое количество слов
        text = '«Школа злословия» учит прикусить язык'
        tf_dict = self.tf_idf.get_count_tf(text)
        tf_idf_dict = self.tf_idf.count_tf_idf(text)
        self.assertEqual(len(tf_dict), len(tf_idf_dict))

    def test_not_empty(self):  # проверяем, что файл непустой
        idf_dict = self.tf_idf.get_load('idf.json')
        self.assertGreater(len(idf_dict), 0)


if __name__ == '__main__':
    unittest.main()
