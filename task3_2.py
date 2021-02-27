import json
with open('RomeoAndJuliet.json', 'r') as f1:
    piece = json.load(f1)
list_of_characters = []  # список всех персонажей пьесы (сгруппированы по сценам)
acts = piece['acts']  # список всех актов пьесы
for act in acts:  # в цикле перебираем акты пьесы (это словари)
    scenes = act['scenes']  # для каждого акта задаём список сцен
    for scene in scenes:  # в цикле перебираем все сцены данного акта
        characters = []  # определяем список действующих лиц - для каждой сцены он свой
        for scene in scenes:  # перебираем сцены в цикле
            action = scene['action']  # это список из словарей; в каждом словаре по 2 ключа:
            # "character" (они нам и нужны) и "says"
            for a in action:
                characters.append(a['character'])
        list_of_characters.append(list(set(characters)))  # избавляемся от повторов, затем обратно
        # превращаем множество в список и добавляем его к общему списку персонажей
with open('characters.json', 'w') as f2:
    for scene in list_of_characters:
        new_str = json.dumps(scene)
        f2.write(new_str + '\n')
