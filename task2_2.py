import csv
with open('stage3_test.csv') as csvfile1:
    spamreader = csv.reader(csvfile1, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    with open('2.csv', 'w') as csvfile2:
        fieldnames = ['Id', 'Images', 'Title', 'Description', 'Price']
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        for row in spamreader:
            if row[-1] != 'Price':  # проверяем, что последний объект списка - не слово Price (это так
                #  только для списка с названиями столбцов => программа падает с ошибкой
                price = float(row[-1])
                if 10000 < price <= 50000:  # проверяем, попадает ли цена в диапазон от 10 тысяч до 50 тысяч
                    writer.writerow({'Id': row[0], 'Images': row[1], 'Title': row[2],
                                     'Description': row[3], 'Price': row[4]})  # если да, записываю
                    # этот продукт в новый файл
