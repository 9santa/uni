import csv

result = []
with open('hw20/web_clients_correct.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    for row in csv_reader:
        temp = "Пользователь " + row[0]
        if (row[3] == 'female'): temp += " женского пола,"
        else: temp += " мужского пола,"
        temp += ' ' + row[4] + " лет,"
        temp += " совершила покупку на " + row[5] + " у.е"
        if (row[1] == 'mobile'):
            temp += " с мобильного браузера " + row[2] + '.'
        else:
            temp += " с бразузера " + row[2] + '.'
        temp += " Регион, из которого совершалась покупка: " + row[6] + '.'

        result.append(temp)

print(result[0])