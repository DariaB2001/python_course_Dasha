import xml.etree.ElementTree as etree


class Corpus():

    def __init__(self):
        self._sentences = []  # список всех предложений корпуса

    def load(self, filename):
        tree = etree.parse(filename)
        root = tree.getroot()  # корневой объект
        for sentence in root.iter('sentence'):  # перебираем все предложения корпуса
            sentence_str = sentence.find('source').text  # строковое представление предложения
            final_sentence = Sentence(sentence_str)  # создаём предложение - объект класса Sentence
            sentences_raw = sentence.findall('tokens')
            for sentence_raw in sentences_raw:
                tokens = sentence_raw.findall('token')
                for token in tokens:
                    word_str = token.get('text')  # строковое представление слова
                    word = Word(word_str)
                    for g in token.iter('g'):
                        word._grams.append(g.get('v'))  # добавляем граммемы в список _grams
                    final_sentence._words.append(word)  # добавляем слово к списку слов для данного предложения

            self._sentences.append(final_sentence)

    def get_sentence_by_id(self, id=None):
        if id == None:
            id = int(input('Введите номер предложения: '))
        if id >= 0 and id < len(self._sentences):
            return self._sentences[id]
        else:
            print('Некорректный номер предложения')
            return None


class Sentence():

    def __init__(self, sentence_str):
        self._words = []  # списое слов предложения
        self._sentence_str = sentence_str  # строковое представление предложения

    def get_word_by_id(self, id=None):
        if id == None:
            id=int(input('Введите номер слова: '))
        if id >= 0 and id < len(self._words):
            return self._words[id]
        else:
            print('Некорректный номер слова')
            return None


class Word():

    def __init__(self, word_str):
        self._grams = []  # список граммем слова
        self._word_str = word_str  # строковое представление слова

    def get_grammar_by_id(self, id=None):
        if id == None:
            id=int(input('Введите номер граммемы: '))
        if id >= 0 and id < len(self._grams):
            return self._grams[id]
        else:
            print('Некорректный номер граммемы')
            return None


if __name__ == '__main__':
    corpus = Corpus()
    corpus.load('annot.opcorpora.no_ambig.xml')
    sentence = corpus.get_sentence_by_id(0)
    word = sentence.get_word_by_id(0)
    grammar = word.get_grammar_by_id(0)
    print(sentence._sentence_str)
    print(word._word_str)
    print(grammar)
