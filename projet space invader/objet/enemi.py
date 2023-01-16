from PIL import Image, ImageTk
from tkinter import messagebox
class enemi:
    def __init__(self,canvas):
        self.enemi_coord_x=10
        self.enemi_coord_y=20
        self.enemi_hauteur=30
        self.enemi_largeur=30
        self.nb_enemi=7
        self.liste_enemi=[]
        self.vitesse=1
        self.side=0

    #fonction creation d'enemi forme simple
    def creation_enemi(self,canvas, alien_image):
        #self.e_id=canvas.create_rectangle(self.enemi_coord_x,
         #                           self.enemi_coord_y,
          #                          self.enemi_coord_x+self.enemi_hauteur,
           #                         self.enemi_coord_y+self.enemi_largeur,
            #                        outline="#000000", fill="#FF0000")
        # for i in range(self.nb_enemi):
        #     self.e_id2 =  canvas.create_rectangle(
        #                         self.enemi_coord_x+i*100,
        #                         self.enemi_coord_y, 
        #                         self.enemi_coord_x+i*100 + self.enemi_largeur, 
        #                         self.enemi_coord_y + self.enemi_largeur, 
        #                         outline="#000000", fill="#FF0000")
        #     self.liste_enemi.append(self.e_id2)
        for i in range(self.nb_enemi):
            self.e_id2 =  canvas.create_image(
                                self.enemi_coord_x+i*100,
                                self.enemi_coord_y,
                                image=alien_image, anchor="nw")
            self.liste_enemi.append(self.e_id2)
        return self.liste_enemi


                

#fonction qui fait bouger un groupe d enemi image
    def movement(self,canvas):
        bas=0
        for i,val in enumerate(self.liste_enemi):
            if self.side%2==0:
                move=2
                cote=1
                (x_e_0,y_e_0,x_e_1,y_e_1)=canvas.bbox(self.liste_enemi[-1])
                if x_e_1==700:
                    self.side=self.side+1
                    bas=30      
            if self.side%2==1:
                move=-2
                cote=-1
                (x_e_0,y_e_0,x_e_1,y_e_1)=canvas.bbox(self.liste_enemi[0])
                if x_e_0==0:
                    self.side=self.side+1
            canvas.move(self.liste_enemi[i],2*cote,bas)
            (x_ed_0,y_ed_0,x_ed_1,y_ed_1)=canvas.bbox(self.liste_enemi[0])
            if y_ed_0==650:
                break
                
        