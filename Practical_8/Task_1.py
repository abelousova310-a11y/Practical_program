print("Таблица умножения на n")

n = int(input("Введите положительное натуральное число:"))
for i in range(1,11):
    result = n * i
print(f"{n} x {i} = {result}")
