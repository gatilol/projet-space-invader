from re import X
from tkinter import Y
from objet.joueur import joueur
from objet.enemi import enemi


class projectil:
    def __init__(self,canvas):
        self.projectil_coord_x=0
        self.projectil_coord_y=0
        self.projectil_hauteur=30
        self.projectil_largeur=5

    def creation_projectil_joueur(self,canvas,X,Y):
        self.projectil_coord_x=X
        self.projectil_coord_y=Y
        self.pj_id=canvas.create_rectangle(self.projectil_coord_x,
                                    self.projectil_coord_y,
                                    self.projectil_coord_x+self.projectil_hauteur,
                                    self.projectil_coord_y+self.projectil_largeur,
                                    outline="#fb0", fill="#fb0")
        return self.pj_id


    def getcoordx(self):
        return self.projectil_coord_x
    
    def getlargeur(self):
        return self.projectil_largeur
    
    def getcoordy(self):
        return self.projectil_coord_y
    
    def gethauteur(self):
        return self.projectil_hauteur




    def deplacement_proj_joueur(self,canvas):
        canvas.move(self.pj_id,0,3)
        if self.projectil_coord_y>0 :
            canvas.after(10 ,deplacement_proj_joueur(canvas))
        else :
            canvas.delete(self.pj_id)
