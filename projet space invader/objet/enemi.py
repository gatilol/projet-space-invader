from PIL import Image, ImageTk

class enemi:
    def __init__(self,canvas):
        self.enemi_coord_x=10
        self.enemi_coord_y=20
        self.enemi_hauteur=30
        self.enemi_largeur=30
        self.nb_enemi=7
        self.liste_enemi=[]
        self.vitesse=1

    #fonction creation d'enemi forme simple
    def creation_enemi(self,canvas):
        #self.e_id=canvas.create_rectangle(self.enemi_coord_x,
         #                           self.enemi_coord_y,
          #                          self.enemi_coord_x+self.enemi_hauteur,
           #                         self.enemi_coord_y+self.enemi_largeur,
            #                        outline="#000000", fill="#FF0000")
        for i in range(self.nb_enemi):
            self.e_id2 =  canvas.create_rectangle(
                                self.enemi_coord_x+i*100,
                                self.enemi_coord_y, 
                                self.enemi_coord_x+i*100 + self.enemi_largeur, 
                                self.enemi_coord_y + self.enemi_largeur, 
                                outline="#000000", fill="#FF0000")
            self.liste_enemi.append(self.e_id2)
        return self.e_id2

        def enemi_move2(canvas):
            (x_e_0,y_e_0,x_e_1,y_e_1)=canvas.coords(self.e_id2)
            bas=0
            global side
            side=0
            len=nb_enemi_en_vie()
            for i in range(len(slen)):
                if side%2==0:
                    move=2
                    if canvas.coords(self.liste_enemi[len][2])==700:
                        side=side+1     
                if side%2==1:
                    move=-2
                    if canvas.coords(self.liste_enemi[0][0])==0:
                        side=side+1
                        bas=30      
                Can.move(self.liste_enemi[i],move,bas)
                
    #retourn le nombre d'enemi sur la ligne
    def nb_enemi_en_vie(self):
        return len(self.liste_enemi)
    #Imgalien=ImageTk.PhotoImage(Image.open("projet space invader\image\Alien.png"))
    #fonction creation d'enemi en image
    def creation_enemi2(self,canvas,images):
        self.e_id=ship=canvas.create_image(self.enemi_coord_x+15,
                                    self.enemi_coord_y+15,
                                    image=images)
        return self.e_id
    



    #def movement(self):
    #    side=0
    #    #changement de direction
    #   if self.enemi_coord_x==690:
    #        side+=1
    #    if self.enemi_coord_x==0:
    #        side+=1
    #    #movement vers la droite
    #    if side==0%2 and self.enemi_coord_x!=690:
    #        self.enemi_coord_x= self.enemi_coord_x + self.vitesse*self.enemi_largeur
    #    #movement vers la gauche
    #    if side==1%2 and self.enemi_coord_x!=0:
    #        self.enemi_coord_x= self.enemi_coord_x - self.vitesse*self.enemi_largeur


