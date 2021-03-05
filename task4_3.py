import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
conj = 0  # счётчик для слова "может" в функции союза
verb = 0  # счётчик для слова "может" в функции глагола
for token in root.iter('token'):  # перебираем все слова файла
    if token.get('text').lower() == 'может':  # рассматриваем только слова "может"
        for g in token.iter('g'):  # рассматриваем грамматическую информацию для данного слова
            if g.get('v') == 'CONJ':  # если это союз
                conj += 1  # увеличиваем союзный
            elif g.get('v') == 'VERB':
                verb += 1
print('В качестве союза слово "может" встречается ' + str(conj) + ' раз')
print('В качестве глагола слово "может" встречается ' + str(verb) + ' раз')
