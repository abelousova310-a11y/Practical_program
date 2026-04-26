n = int(input("Введите натуральное число n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i
print(f"Знакопеременная сумма от 1 до {n} равна: {total}")
