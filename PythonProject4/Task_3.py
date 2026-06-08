#Задача: Бестиарий. Часть 3 (Битва монстров)
class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстер: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")

data1 = input("Введите первого монстра: ").split()
data2 = input("Введите второго монстра: ").split()

m1 = Monster(data1[0], int(data1[1]), int(data1[2]))
m2 = Monster(data2[0], int(data2[1]), int(data2[2]))

while True:
    print(f"{m1.name} наносит удар!")
    m2.hp -= m1.dmg
    if m2.hp < 0:
        m2.hp = 0
        print(f"У {m2.name} осталось {m2.hp}")

    if m2.hp == 0:
        print(f"Победил {m1.name}!")
        break

    print(f"{m2.name} наносит удар!")
    m1.hp -= m2.dmg
    if m1.hp < 0:
        m1.hp = 0
        print(f"У {m1.name} осталось {m1.hp}")

    if m1.hp == 0:
        print(f"Победил {m2.name}!")
        break