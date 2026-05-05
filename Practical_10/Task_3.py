max_number = 0

while True:
    number = int(input("Введите натуральное число: "))
    if number == 0:
        break
    if number > max_number:
        max_number = number

print(max_number)
