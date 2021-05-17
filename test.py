import unittest
from morphology import Corpus


class MyTestCase(unittest.TestCase):
    def setUp(self):
        corpus = Corpus()
        corpus.load('annot.opcorpora.no_ambig.xml')
        self.sentence = corpus.get_sentence_by_id(id=0)

    def test_presence_words_in_sentence(self):
        self.assertGreater(len(self.sentence._words), 0)

    def test_first_sentence(self):
        self.assertEqual(self.sentence._sentence_str, '«Школа злословия» учит прикусить язык')

    def test_grammar(self):
        word = self.sentence.get_word_by_id(1)
        self.assertIn('NOUN', word._grams)


if __name__ == '__main__':
    unittest.main()
