from .Player import Player

class World:
    PLAYER_COORD_X=40
    PLAYER_COORD_Y=40
    PLAYER_HEIGHT=10
    PLAYER_WIDTH=50

    def __init__(self, canvas):
        self.init_World(canvas)

    def init_World(self,canvas):
        p = Player(self.PLAYER_COORD_X,
                    self.PLAYER_COORD_X,
                    self.PLAYER_WIDTH,
                    self.PLAYER_HEIGHT)
        p.first_display(canvas)
        self.p = p

        
