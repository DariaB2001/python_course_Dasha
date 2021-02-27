import csv
with open('stage3_test.csv') as csvfile1:
    reader = csv.DictReader(csvfile1)
    with open('3.csv', 'w') as csvfile2:
        fieldnames = ['Id', 'Title', 'Price']
        writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow({'Id': row['Id'], 'Title': row['Title'], 'Price': row['Price']})
