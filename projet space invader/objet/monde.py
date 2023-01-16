from .joueur import joueur
from .enemi import enemi
from .projectil import projectil
from .protection import protection

class Monde: 
#classe qui initialisé le jeu
    def __init__(self,canvas, alien_image):
        self.init_monde(canvas, alien_image)


    def init_monde(self,canvas, alien_image):
        #j=joueur(canvas)
        #j.creation_joueur(canvas)
        #self.joueur=j

        e=enemi(canvas)
        e.creation_enemi(canvas, alien_image)
        self.enemi=e
        

        pr=protection(canvas)
        pr.creation_protection(canvas)
        self.protection=pr
