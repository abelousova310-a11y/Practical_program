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

class Vampire(Monster):
    def __init__(self, name = "Vampire"):
        super().__init__(name, 80, 15)

    def take_damage(self, damage):
        attacks_damage = damage - 5
        self.hp -= attacks_damage
        print(f"{self.name} поглощает 5 урона! Получено: {attacks_damage}. HP: {self.hp}")

class Ghost(Monster):
    def __init__(self, name = "Ghost"):
        super().__init__(name, 60, 20)

    def take_damage(self, damage):
        import random
        if random.random() < 0.3:
            print(f"{self.name()} 30% шанс уклонится от удара")
        else:
            self.hp -= damage
            print(f"{self.name()} получает {damage}. HP: {self.hp}")

class Werewolf(Monster):
    def __init__(self, name = "Werewolf"):
        super().__init__(name, 100, 25)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} получает {damage}. HP: {self.hp}")
        if self.hp < 50:
            print(f"{self.name} трансфармируется")
v = Vampire("Дракула")
v.take_damage(30)
#Дракула поглощает 5 урона! Получено: 25. HP: 55

z = Zombie("Зомби")
z.take_damage(30)
#Зомби теряет конечность! Получено: 30. HP: 90