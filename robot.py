from weapon import Weapon


class Robot:
    def __init__(self):
        self.name = ''
        self.health = ''
        self.power_level = ''
        self.weapon = Weapon()

    def attack_with_weapon(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(self.name + ' shot ' + dinosaur.name)


