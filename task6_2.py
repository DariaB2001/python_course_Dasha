import collections
import json
d = collections.defaultdict(list)
with open('RomeoAndJuliet.json', 'r') as f1:
    piece = json.load(f1)
s = []  # список, который содержит кортежи вида (персонаж, его реплика)
acts = piece['acts']  # список всех актов пьесы
for act in acts:  # в цикле перебираем акты пьесы (это словари)
    scenes = act['scenes']  # для каждого акта задаём список сцен
    for scene in scenes:  # в цикле перебираем все сцены данного акта
        action = scene['action']  # это список из словарей; в каждом словаре по 2 ключа:
        # "character" (то есть имя персонажа) и "says" (то есть его реплика)
        for a in action:
            s.append((a['character'], a['says']))  # добавляем к списку s кортеж вида (персонаж, его реплика)
for k, v in s:  # в цикле перебираем элементы списка s - кортежи
    d[k].append(v)
with open('character_says.json', 'w') as f2:
    json.dump(d, f2)
