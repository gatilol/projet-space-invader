
class joueur:
    def __init__(self,canvas):
        self.joueur_coord_x=20
        self.joueur_coord_y=650
        self.joueur_hauteur=25
        self.joueur_largeur=25

    def creation_joueur(self,canvas):
        self.j_id=canvas.create_rectangle(self.joueur_coord_x,
                                    self.joueur_coord_y,
                                    self.joueur_coord_x+self.joueur_hauteur,
                                    self.joueur_coord_y+self.joueur_largeur,
                                    outline="#fb0", fill="#fb0")
        return self.j_id

    def mvt_joueur(self,canvas):
        pass


