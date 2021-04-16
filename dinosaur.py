class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = ''
        self.energy = ''
        self.attack_power = ''

    def attack(self, player_loses_health_pts):
        player_loses_health_pts.attack = self.receive_attack()

    def receive_attack(self):
        print('OUCH!')
        return 'has been hit'
