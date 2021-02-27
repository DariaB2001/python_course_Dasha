import json

with open('wikidata_1000.json', 'r') as f:
    lines = []
    for line in f:
        lines.append(json.loads(line))
my_dict = {}
for l in lines:
    word = l['label']['value']
    if 'description' in l.keys():
        desc = l['description']['value']
    else:
        desc = None
    my_dict[word] = desc
with open('new_dict.json', 'w') as f_write:
    json.dump(my_dict, f_write)
