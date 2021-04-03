import collections
import csv
with open('stage3_test.csv') as csvfile1:
    reader = csv.DictReader(csvfile1)
    d = {}
    for row in reader:  # перебираем строки в файле
        d[row['Title']] = row['Price']
    sorted_dict1 = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1]))  # сортировка по возрастанию
    items1 = sorted_dict1.items()  # список из кортежей (ключ, значение) словаря sorted_dist1
    sorted_dict2 = collections.OrderedDict(sorted(d.items(), key=lambda t: t[1], reverse=True))  # сортировка
    # по убыванию
    items2 = sorted_dict2.items()  # список из кортежей (ключ, значение) словаря sorted_dist2
    with open('2.csv', 'w') as csvfile2:  # открываем файл на запись
        fieldnames = ['Title', 'Price']  # в этом файле только 2 колонки: Title и Price
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        for t in items1:  # перебираем кортежи (ключ, значение)
            writer.writerow({'Title': t[0], 'Price': t[1]})
    with open('3.csv', 'w') as csvfile3:
        fieldnames = ['Title', 'Price']
        writer = csv.DictWriter(csvfile3, fieldnames=fieldnames)
        writer.writeheader()
        for t in items2:
            writer.writerow({'Title': t[0], 'Price': t[1]})
