first_number = int(input())

while True:
    second_number = int(input())
    if second_number > first_number:
        break
    else:
        print("Ошибка. Введите второе число заново")

while True:
    third_number = int(input())
    if third_number > second_number:
        break
    else:
        print("Ошибка. Введите третье число заново")

print("Последовательность принята")
