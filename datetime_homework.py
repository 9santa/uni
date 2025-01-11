from datetime import datetime

s = ""
while(s != "S"):
    s = input()
    format1 = '%A, %B %d, %Y'
    format2 = '%A, %d.%m.%y'
    format3 = '%A, %d %B %Y'
    if s != "End":
        date1 = datetime.strptime(s, format1)
        date2 = datetime.strptime(s, format2)
        date3 = datetime.strptime(s, format3)
        print(date1, date2, date3)

# print(date)