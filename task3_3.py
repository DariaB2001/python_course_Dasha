"Здесь всё очень некрасиво, но не знаю, как оптимизировать"
import json
with open('RomeoAndJuliet.json', 'r') as f1:
    piece = json.load(f1)
number_of_phrases = {}  # словарь, в котором ключи - это имена персонажей,
# а значения - количество фраз соответствующего персонажа
acts = piece['acts']  # список всех актов пьесы
for act in acts:  # в цикле перебираем акты пьесы (это словари)
    scenes = act['scenes']  # для каждого акта задаём список сцен
    for scene in scenes:  # в цикле перебираем все сцены данного акта
        for scene in scenes:  # перебираем сцены в цикле
            action = scene['action']  # это список из словарей; в каждом словаре по 2 ключа:
            # "character" и "says"
            for a in action:
                if a['character'] in number_of_phrases.keys():
                    number_of_phrases[a['character']] += 1
                else:
                    number_of_phrases[a['character']] = 1
persons = {}  # новый словарь, в котором ключи и значений меняются местами
for person in number_of_phrases.keys():
    persons[number_of_phrases[person]] = person
print('Самый болтливый персонаж - это ' + persons[max(persons.keys())])
