correct_pin = 4590

while True:
    pin = int(input())
    if pin == correct_pin:
        print("Доступ разрешен")
        break
    else:
        print("Ошибка. Попробуйте еще раз")
