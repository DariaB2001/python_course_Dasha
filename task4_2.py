import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
nouns_plural = []
with open('nouns_plural.txt', 'w') as f:
    for token in root.iter('token'):
        grammar = []  # грамматическая информация для каждого элемента token
        for g in token.iter('g'):
            grammar.append(g.get('v'))
        if 'NOUN' in grammar and 'plur' in grammar:
            f.write(token.get('text') + ', ')
