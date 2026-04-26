# Ввод начальных данных
m = int(input("Введите стартовое количество организмов (m): "))
p = int(input("Введите среднесуточное увеличение в процентах (p): "))
n = int(input("Введите количество дней для размножения (n): "))

current_population = m

for day in range(1, n + 1):
    print(f"{day} {current_population:}")
    current_population = current_population * (1 + p / 100)