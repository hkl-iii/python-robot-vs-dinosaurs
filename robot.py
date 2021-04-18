from armory import Armory



class Robot:
    def __init__(self):
        self.name = ''
        self.health = ''
        self.power_level = ''
        self.weapon = Armory.Weapon()

    def attack_with_weapon(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        self.power_level -= 10
        print(self.name + ' shot ' + dinosaur.name)


