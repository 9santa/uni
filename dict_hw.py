# исходные данные
items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9 },
 'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
 'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}

# итоговый словарь
price_list = {}
# перебираем внутренний словарь и смотрим значение count
for key, value in items.items():
    if (value['count'] < 20):
        price_list[key] = True
    else:
        price_list[key] = False
    
        
print(price_list)
