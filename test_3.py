import unittest
import os
import shutil


def make_file_in_folder(path):
    global d
    os.mkdir(path)
    d = os.path.join('Home/PycharmProjects/python_course_Dasha/new_folder', '1.txt')
    with open(d, 'w') as f:
        f.write('text in the file')


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        make_file_in_folder('Home/PycharmProjects/python_course_Dasha/new_folder')

    def test_file(self):
        with open(d,'r') as f1:
            text = f1.read()
        self.assertEqual(text, 'text in the file')

    def tearDown(self) -> None:
        shutil.rmtree('Home/PycharmProjects/python_course_Dasha/new_folder')


if __name__ == '__main__':
    unittest.main()
