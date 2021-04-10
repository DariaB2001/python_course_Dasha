import csv
import collections
cnt = collections.Counter()
with open('stage3_test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    words = []  # список всех слов из файла
    for row in reader:  # перебираем строки в файле
        for word in row['Title'].split():
            w = word.lower().strip(',.!?')
            cnt[w] += 1  # учитываем в счётчике все слова из колонки Title
        for word in row['Description'].split():
            w = word.lower().strip(',.!?')
            cnt[w] += 1  # учитываем в счётчике все слова из колонки Description
print(cnt.most_common(20))  # наиболее часто встречающиеся слова
print(cnt.most_common()[::-1][:20])  # наиболее редко встречающиеся слова
