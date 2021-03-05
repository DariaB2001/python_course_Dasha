import xml.etree.ElementTree as etree
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
with open('phrases.txt', 'w') as f:
    for source in root.iter('source'):
        p = source.text
        f.write(p + '\n')
