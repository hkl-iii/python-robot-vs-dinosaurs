from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        match_over = False
        while match_over:
            if Fleet.health == 0:
                match_over = True
                del self
                print('DINOSAURS WIN!')
                print('GAME OVER')
            elif Herd.health == 0:
                match_over = True
                print('ROBOTS WIN!')
                print('GAME OVER')
                del self






