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
        self.listproj=[]

    def creation_projectil_joueur(self,canvas,X,Y):
        self.projectil_coord_x=X
        self.projectil_coord_y=Y
        self.pj_id=canvas.create_rectangle(self.projectil_coord_x,
                                    self.projectil_coord_y,
                                    self.projectil_coord_x+self.projectil_largeur,
                                    self.projectil_coord_y+self.projectil_hauteur,
                                    outline="#fb0", fill="#fb0")








    def deplacement_proj_joueur(self,canvas):
        b=0
        canvas.move(self.pj_id,0,-5) 
        (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(self.pj_id)
        if y_p_1<=0:
            canvas.delete(self.pj_id)
            b=1
        return b