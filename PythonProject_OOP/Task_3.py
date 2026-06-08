class Monster:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

class Zombie(Monster):
    def __init__(self, name = "Зомби"):
        super().__init__(name, 120, 10)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} теряет конечность! Получено: {self.dmg}. HP: {self.hp}")

class Weapon:
    def __init__(self, name):
        self.name = name

class SilverSword(Weapon):
    def __init__(self, name = "Серебрянный меч"):
        super().__init__(name)

    def use(self, monster):
        print(f"{self.name} наносит {monster.name} 30 урона")
        monster.take_damage(30)

class HolyWater(Weapon):
    def __init__(self, name = "Святая вода"):
        super().__init__(name)

    def use(self, monster):
        print(f"{self.name} наносит {monster.name} 20 урона")
        monster.take_damage(20)

class CrossbowBolt(Weapon):
    def __init__(self, name = "Арбалет с болтом"):
        super().__init__(name)

    def use(self, monster):
        print(f"{self.name} наносит {monster.name} 25 урона")
        monster.take_damage(25)
weapons = [SilverSword(), HolyWater(), CrossbowBolt()]
zombie = Zombie("Зомби")
for w in weapons:
    w.use(zombie)
# Полиморфизм: один цикл — три разных удара!