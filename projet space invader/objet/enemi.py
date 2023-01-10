class enemi:
    def __init__(self,canvas):
        self.enemi_coord_x=150
        self.enemi_coord_y=30
        self.enemi_hauteur=30
        self.enemi_largeur=30


    def creation_enemi(self,canvas):
        self.j_id=canvas.create_rectangle(self.enemi_coord_x,
                                    self.enemi_coord_y,
                                    self.enemi_coord_x+self.enemi_hauteur,
                                    self.enemi_coord_y+self.enemi_largeur,
                                    outline="#000000", fill="#FF0000")
        return self.j_id


    def getcoordx(self):
        return self.enemi_coord_x
    
    def getlargeur(self):
        return self.enemi_largeur
    
    def getcoordy(self):
        return self.enemi_coord_y
    
    def gethauteur(self):
        return self.enemi_hauteur