from robot import Robot


class fleet:

    def __init__(self):
        robot_1 = Robot()
        robot_1.name = 'R-800'
        robot_1.health = 100
        robot_1.power_level = 5
        robot_1.weapon = 'pistol'

        robot_2 = Robot()
        robot_2.name = 'R-1000'
        robot_2.health = 100
        robot_2.power_level = 10
        robot_2.weapon = 'shotgun'

        robot_3 = Robot()
        robot_3.name = 'Mega-RX'
        robot_3.health = 150
        robot_3.power_level = 15
        robot_3.weapon = 'tommy gun'
