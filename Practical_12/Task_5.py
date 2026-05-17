data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
last_three = data[-3:]
reversed_list = data[::-1]
odd_indices = data[1::2]        

print(f"Первая тройка: {first_three}")
print(f"Последняя тройка: {last_three}")
print(f"В обратном порядке: {reversed_list}")
print(f"Элементы с нечётными индексами: {odd_indices}")