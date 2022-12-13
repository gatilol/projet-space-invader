class projectil:
    def __init__(self,canvas):
        self.projectil_coord_x=20
        self.projectil_coord_y=300
        self.projectil_hauteur=5
        self.projectil_largeur=30

    def creation_projectil(self,canvas):
        self.j_id=canvas.create_rectangle(self.projectil_coord_x,
                                    self.projectil_coord_y,
                                    self.projectil_coord_x+self.projectil_hauteur,
                                    self.projectil_coord_y+self.projectil_largeur,
                                    outline="#fb0", fill="#fb0")
        return self.j_id