from re import X
from tkinter import Y
from objet.protection import protection


class projectil:
    def __init__(self,canvas):
        self.projectil_coord_x=0
        self.projectil_coord_y=0
        self.projectil_hauteur=30
        self.projectil_largeur=5
        self.listproj=[]

#creation des projectil
    def creation_projectil_joueur(self,canvas,X,Y):
        self.projectil_coord_x=X
        self.projectil_coord_y=Y
        self.pj_id=canvas.create_rectangle(self.projectil_coord_x,
                                    self.projectil_coord_y,
                                    self.projectil_coord_x+self.projectil_largeur,
                                    self.projectil_coord_y+self.projectil_hauteur,
                                    outline="#fb0", fill="#fb0")







#fonction qui fait bouger le projectil du joueur
    def deplacement_proj_joueur(self,canvas):
        b=0
        canvas.move(self.pj_id,0,-5) 
        (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(self.pj_id)
        if y_p_1<=0:
            canvas.delete(self.pj_id)
            b=1
        return b

#fonction qui fait les colisions des missiles
    def veriftoucherprotectj(self,canvas,fullprotect):
        b=0
        (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(self.pj_id)
        for i,tblock in enumerate(fullprotect):
            for v,block in enumerate(tblock):
                for w,prot in enumerate(block):
                    (x_0,y_0,x_1,y_1)=canvas.coords(prot)
                    
                    if x_0<x_p_0<x_1 and x_0<x_p_1<x_1 and y_0<y_p_0<y_1 :
                        canvas.delete(self.pj_id)
                        canvas.delete(prot)

                        b=1
                        fullprotect[i][v].pop(w)
        return b

    def veriftoucherenemi(self,canvas,listenemi):
        b=0
        (x_p_0,y_p_0,x_p_1,y_p_1)=canvas.coords(self.pj_id)
        for i,enemi in enumerate(listenemi):
            (x_0,y_0,x_1,y_1)=canvas.coords(enemi)
            if x_0<x_p_0<x_1 and x_0<x_p_1<x_1 and y_0<y_p_0<y_1 :
                canvas.delete(self.pj_id)
                canvas.delete(enemi)

                b=1
        return b