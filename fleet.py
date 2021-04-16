from robot import Robot


class Fleet:

    def __init__(self):
        robot_1 = Robot()
        robot_1.name = 'R-800'
        robot_1.health = 100
        robot_1.power_level = 100

        robot_2 = Robot()
        robot_2.name = 'R-1000'
        robot_2.health = 100
        robot_2.power_level = 100

        robot_3 = Robot()
        robot_3.name = 'Mega-RX'
        robot_3.health = 150
        robot_3.power_level = 150
