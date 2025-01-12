import csv

url = 'web_clients_correct.csv'
with open(url, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    for row in csv_reader:
        print(row)