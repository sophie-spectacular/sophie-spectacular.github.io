import numpy as np

class Map:
    def __init__(self):
        self.map = np.zeros((100, 100))
        self.position = [50, 50]
        self.direction = 'south'

    def turn(direction: str):
        if direction == 'left':
            if self.direction == 'south':
                self.direction == 'east'
            elif self.direction == 'east':
                self.direction == 'north'
            elif self.direction == 'north':
                self.direction == 'west'
            elif self.direction == 'west':
                self.direction == 'south'
        elif direction == 'right':
            if self.direction == 'south':
                self.direction == 'west'
            elif self.direction == 'west':
                self.direction == 'north'
            elif self.direction == 'north':
                self.direction == 'east'
            elif self.direction == 'east':
                self.direction == 'south'
    
    def forward(steps: int):
        try:
            return
        except:
            print('You have fallen off the map. You will respawn at start.')
            self.__init__()
            