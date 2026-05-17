prices = [1500, 500, 2000, 3500, 1000, 4500]

max_price = max(prices)
min_price = min(prices)
total_price = sum(prices)
average_price = total_price / len(prices)

print(f"Самый дорогой товар: {max_price}")
print(f"Самый дешёвый товар: {min_price}")
print(f"Общая стоимость: {total_price}")
print(f"Средняя цена: {average_price:.2f}")