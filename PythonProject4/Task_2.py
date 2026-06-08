#Задача: Бестиарий. Часть 2 (Ввод данных)
class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстер: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")

data1 = input().split()
data2 = input().split()

m1 = Monster(data1[0], data1[1], data1[2])
m2 = Monster(data2[0], data2[1], data2[2])