"Здесь всё очень некрасиво, но не знаю, как оптимизировать"
import json
with open('RomeoAndJuliet.json', 'r') as f1:
    piece = json.load(f1)
p1 = 0  # FRIAR LAURENCE
p2 = 0  # Second Servant
p3 = 0  # ROMEO
p4 = 0  # GREGORY
p5 = 0  # CAPULET
p6 = 0  # BENVOLIO
p7 = 0  # First Musician
p8 = 0  # Third Watchman
p9 = 0  # LADY CAPULET
p10 = 0  # Musician
p11 = 0  # Servant
p12 = 0  # PETER
p13 = 0  # MONTAGUE
p14 = 0  # BALTHASAR
p15 = 0  # ABRAHAM
p16 = 0  # SAMPSON
p17 = 0  # PAGE
p18 = 0  # TYBALT
p19 = 0  # Apothecary
p20 = 0  # Nurse
p21 = 0  # Second Musician
p22 = 0  # First Citizen
p23 = 0  # First Watchman
p24 = 0  # Second Watchman
p25 = 0  # Third Musician
p26 = 0  # Second Capulet
p27 = 0  # NURSE
p28 = 0  # PRINCE
p29 = 0  # LADY MONTAGUE
p30 = 0  # FRIAR JOHN
p31 = 0  # JULIET
p32 = 0  # First Servant
p33 = 0  # PARIS
p34 = 0  # MERCUTIO
p35 = 0  # LADY  CAPULET
acts = piece['acts']  # список всех актов пьесы
for act in acts:  # в цикле перебираем акты пьесы (это словари)
    scenes = act['scenes']  # для каждого акта задаём список сцен
    for scene in scenes:  # в цикле перебираем все сцены данного акта
        for scene in scenes:  # перебираем сцены в цикле
            action = scene['action']  # это список из словарей; в каждом словаре по 2 ключа:
            # "character" и "says"
            for a in action:
                if a['character'] == 'FRIAR LAURENCE':
                    p1 += len(a['says'])
                elif a['character'] == 'Second Servant':
                    p2 += len(a['says'])
                elif a['character'] == 'ROMEO':
                    p3 += len(a['says'])
                elif a['character'] == 'GREGORY':
                    p4 += len(a['says'])
                elif a['character'] == 'CAPULET':
                    p5 += len(a['says'])
                elif a['character'] == 'BENVOLIO':
                    p6 += len(a['says'])
                elif a['character'] == 'First Musician':
                    p7 += len(a['says'])
                elif a['character'] == 'Third Watchman':
                    p8 += len(a['says'])
                elif a['character'] == 'LADY CAPULET':
                    p9 += len(a['says'])
                elif a['character'] == 'Musician':
                    p10 += len(a['says'])
                elif a['character'] == 'Servant':
                    p11 += len(a['says'])
                elif a['character'] == 'PETER':
                    p12 += len(a['says'])
                elif a['character'] == 'MONTAGUE':
                    p13 += len(a['says'])
                elif a['character'] == 'BALTHASAR':
                    p14 += len(a['says'])
                elif a['character'] == 'ABRAHAM':
                    p15 += len(a['says'])
                elif a['character'] == 'SAMPSON':
                    p16 += len(a['says'])
                elif a['character'] == 'PAGE':
                    p17 += len(a['says'])
                elif a['character'] == 'TYBALT':
                    p18 += len(a['says'])
                elif a['character'] == 'Apothecary':
                    p19 += len(a['says'])
                elif a['character'] == 'Nurse':
                    p20 += len(a['says'])
                if a['character'] == 'Second Musician':
                    p21 += len(a['says'])
                elif a['character'] == 'First Citizen':
                    p22 += len(a['says'])
                elif a['character'] == 'First Watchman':
                    p23 += len(a['says'])
                elif a['character'] == 'Second Watchman':
                    p24 += len(a['says'])
                elif a['character'] == 'Third Musician':
                    p25 += len(a['says'])
                elif a['character'] == 'Second Capulet':
                    p26 += len(a['says'])
                elif a['character'] == 'NURSE':
                    p27 += len(a['says'])
                elif a['character'] == 'PRINCE':
                    p28 += len(a['says'])
                elif a['character'] == 'LADY MONTAGUE':
                    p29 += len(a['says'])
                elif a['character'] == 'FRIAR JOHN':
                    p30 += len(a['says'])
                if a['character'] == 'JULIET':
                    p31 += len(a['says'])
                elif a['character'] == 'First Servant':
                    p32 += len(a['says'])
                elif a['character'] == 'PARIS':
                    p33 += len(a['says'])
                elif a['character'] == 'MERCUTIO':
                    p34 += len(a['says'])
                elif a['character'] == 'LADY  CAPULET':
                    p35 += len(a['says'])
persons = {p1: 'FRIAR LAURENCE', p2: 'Second Servant', p3: 'ROMEO', p4: 'GREGORY', p5: 'CAPULET', p6: 'BENVOLIO',
    p7: 'First Musician', p8: 'Third Watchman', p9: 'LADY CAPULET', p10: 'Musician', p11: 'Servant', p12: 'PETER',
    p13: 'MONTAGUE', p14: 'BALTHASAR', p15: 'ABRAHAM', p16: 'SAMPSON', p17: 'PAGE', p18: 'TYBALT', p19: 'Apothecary',
    p20: 'Nurse', p21: 'Second Musician', p22: 'First Citizen', p23: 'First Watchman', p24: 'Second Watchman',
    p25: 'Third Musician', p26: 'Second Capulet', p27: 'NURSE', p28: 'PRINCE', p29: 'LADY MONTAGUE', p30: 'FRIAR JOHN',
    p31: 'JULIET', p32: 'First Servant', p33: 'PARIS', p34: 'MERCUTIO', p35: 'LADY  CAPULET'}
print('Самый болтливый персонаж - это ' + persons[max(persons.keys())])
