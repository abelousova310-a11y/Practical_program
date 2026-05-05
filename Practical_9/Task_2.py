count = 0
found_alexandra = False

while True:
    name = input("Введите имя: ")

    if name == "Александра":
        found_alexandra = True
    elif found_alexandra == 1 and name != "Левон":
        count = count + 1
    elif name == "Левон":
        break

print(count)