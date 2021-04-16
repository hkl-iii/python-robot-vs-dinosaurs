class Robot:
    def __init__(self):
        self.name = ''
        self.health = ''
        self.power_level = ''
        self.weapon = ''

    def attack_with_weapon(self, player_loses_health_pts):
        self.weapon.attack = player_loses_health_pts.weapon.attack
        player_loses_health_pts.weapon.attack = self.receive_attack()

    def receive_attack(self):
        print('OUCH!')
        return 'has been hit'
