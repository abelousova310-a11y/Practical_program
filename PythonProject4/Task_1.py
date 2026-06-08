#Задача: Бестиарий. Часть 1 (Создание монстра)
class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        print(f"Монстер: {self.name}")
        print(f"HP: {self.hp}")
        print(f"DMG: {self.dmg}")


m1 = Monster('Дракула', 120, 35)
m2 = Monster('Люкан', 100, 40)



