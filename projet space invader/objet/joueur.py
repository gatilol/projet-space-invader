from PIL import Image, ImageTk
from tkinter import *
class joueur:
    def __init__(self,canvas):
        self.joueur_coord_x=340
        self.joueur_coord_y=650
        self.joueur_hauteur=20
        self.joueur_largeur=20

#fonction qui cree un joueur a forme simple
    def creation_joueur(self,canvas):
        self.j_id=canvas.create_rectangle(self.joueur_coord_x,
                                    self.joueur_coord_y,
                                    self.joueur_coord_x+self.joueur_hauteur,
                                    self.joueur_coord_y+self.joueur_largeur,
                                    outline="#fb0", fill="#fb0")
        return self.j_id

