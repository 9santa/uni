items = int(input("Введите количество товаров: "))
stores = int(input("Введите количество магазинов: "))
item_price = []
store_sum = [0]*stores

for i in range(items):
	str1 = input("Введите товар и его стоимость в разных магазинах через пробел: ")
	item_price.append(str1.split())


for i in range(0,items):
	for j in range(1,stores+1):
		store_sum[j-1] += int(item_price[i][j])
	
for i in range(stores):
	print("Стоиость всех товаров в магазине №", i+1, "=", store_sum[i])

print("Самый выгодный магазин №", store_sum.index(min(store_sum))+1, "со общей суммой", min(store_sum))

