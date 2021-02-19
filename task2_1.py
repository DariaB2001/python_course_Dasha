import csv
with open('stage3_test.csv') as csvfile1:
    reader = csv.DictReader(csvfile1)
    with open('1.csv', 'w') as csvfile2:
        writer = csv.DictWriter(csvfile2, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            if len(row['Images']) > 3:  # если картинок больше, чем 3
                writer.writerow(row)  # то записывю этот продукт в новый файл
