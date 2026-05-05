amount = int(input("Введите сумму оплаты: "))
count = 0

while amount >= 25:
    amount -= 25
    count += 1
while amount >= 10:
    amount -= 10
    count += 1
while amount >= 5:
    amount -= 5
    count += 1
while amount >= 1:
    amount -= 1
    count += 1

print(count)