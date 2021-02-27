import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
nouns_plural = []
for token in root.iter('token'):
    grammar = []  # грамматическая информация для каждого элемента token
    for g in token.iter('g'):
       grammar.append(g.get('v'))
    if 'NOUN' in grammar and 'plur' in grammar:
        nouns_plural.append(token.get('text'))
with open('nouns_plural.txt', 'w') as f:
    for noun in nouns_plural:
        f.write(noun + ', ')
