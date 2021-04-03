import collections
import json
with open('RomeoAndJuliet.json', 'r') as f:
    piece = json.load(f)
characters = []  # список, к которому буду добавлять имя персонажа столько раз, сколько раз он говорит что-нибудь
acts = piece['acts']  # список всех актов пьесы
for act in acts:  # в цикле перебираем акты пьесы (это словари)
    scenes = act['scenes']  # для каждого акта задаём список сцен
    for scene in scenes:  # в цикле перебираем все сцены данного акта
        action = scene['action']  # это список из словарей; в каждом словаре по 2 ключа:
        # "character" (то есть имя персонажа) и "says" (то есть его реплика)
        for a in action:
            characters.append(a['character'])
cnt = collections.Counter()
for c in characters:
    cnt[c] += 1
list_d = list(cnt.items())
list_d.sort(key=lambda t: t[1], reverse=True)
for t in list_d:
    print(t[0], ':', t[1])
