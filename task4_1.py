import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
phrases = []
for source in root.iter('source'):
    p = source.text
    phrases.append(p)
with open('phrases.txt', 'w') as f:
    for phrase in phrases:
        f.write(phrase + '\n')
