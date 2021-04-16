class Dinosaur:
    def __init__(self):
        self.type = ''
        self.health = ''
        self.energy = ''
        self.attack_power = ''

    def attack(self, robot):
        robot.health -= self.attack_power
        self.energy -= 10
        print(self.name + ' attacked ' + robot.name)




