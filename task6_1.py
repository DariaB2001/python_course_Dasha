import csv
import collections
cnt = collections.Counter()
with open('stage3_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    words = []  # список всех слов из файла
    for row in reader:  # перебираем строки в файле
        words.extend(row['Title'].split())  # присоединяем
        # к списку слов все слова из колонки Title
        words.extend(row['Description'].split())  # присоединяем к списку
        # слов все слова из колонки Description
for word in words:
    w = word.lower().strip(',.!?')
    cnt[w] += 1
print(cnt.most_common(20))  # наиболее часто встречающиеся слова
print(cnt.most_common()[::-1][:20])  # наиболее редко встречающиеся слова
