class Monster:
    def __init__(self, name, hp, dmg):
        self.__name = name
        self.__hp = hp
        self.__dmg = dmg

    #Геттер
    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def get_dmg(self):
        return self.__dmg

    #Сеттер
    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def is_alive(self):
        return self.__hp > 0

    def show_status(self):
         print(f"{self.__name} HP: {self.__hp}")

    def take_damage(self, damage):
        self.__hp -= damage
        print(f"{self.__name} получает урона. HP {self.__hp}")

    def attack_hunter(self, hunter):
        hunter.hp -= self.__dmg
m = Monster("Зомби", 100, 10)
m.show_status()
m.set_hp(-50)
m.show_status()
print(m.is_alive())