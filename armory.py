from weapon import Weapon


class Armory:

    def __init__(self):
        weapon_1 = Weapon()
        weapon_1.type = 'pistol'
        weapon_1.attack_power = 10

        weapon_2 = Weapon()
        weapon_2.type = 'tommy'
        weapon_2.attack_power = 20

        weapon_3 = Weapon()
        weapon_3.type = 'shotti'
        weapon_3.attack_power = 33
