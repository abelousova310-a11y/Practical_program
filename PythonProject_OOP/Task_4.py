class Hunter:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.__weapons = []

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp

    def set_hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def get_weapon(self, weapon):
        self.__weapons.append(weapon)

    def show_inventory(self):
        for i, weapon in enumerate(self.__weapons):
            print(f"{i + 1}. {weapon.name}")

    def attack(self, weapon_index, monster):
        if weapon_index < len(self.__weapons):
            self.__weapons[weapon_index].use(monster)

    def is_alive(self):
        return self.__hp > 0



