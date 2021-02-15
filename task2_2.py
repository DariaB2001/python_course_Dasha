import csv
with open('stage3_test.csv') as csvfile1:
    spamreader = csv.reader(csvfile1, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    with open('2.csv', 'w') as csvfile2:
        fieldnames = ['Id', 'Images', 'Title', 'Description', 'Price']
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        new_writer = []  # делаю список из этого странного объекта, потому что со списком проще работать
        for row in spamreader:
            new_writer.append(row)
        new_writer.pop(0)  # удаляю первый элемент списка - список с названиями столбцов
        for new_row in new_writer:  # для каждого продукта проверяю
            price = float(new_row[-1])
            if (10000 < price) and (price <= 50000):  # попадает ли цена в диапазон от 10 тысяч до 50 тысяч
                writer.writerow({'Id': new_row[0], 'Images': new_row[1], 'Title': new_row[2],
                                 'Description': new_row[3], 'Price': new_row[4]})  # если да, записываю
                # этот продукт в новый файл
