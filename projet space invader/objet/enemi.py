class enemi:
    def __init__(self,canvas):
        self.enemi_coord_x=10
        self.enemi_coord_y=20
        self.enemi_hauteur=30
        self.enemi_largeur=30
        self.liste_enemi=[]
        self.vitesse=1

    def creation_enemi(self,canvas):
        self.j_id=canvas.create_rectangle(self.enemi_coord_x,
                                    self.enemi_coord_y,
                                    self.enemi_coord_x+self.enemi_hauteur,
                                    self.enemi_coord_y+self.enemi_largeur,
                                    outline="#000000", fill="#FF0000")
        return self.j_id
    #load de l'image

    #Imgalien=ImageTk.PhotoImage(Image.open("projet space invader\image\alien.png"))
    def creation_enemi2(self):
        self.e_id=ship=Can.create_image(self.enemi_coord_x,self.enemi_coord_y,image=Imgalien)
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


