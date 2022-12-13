from .joueur import joueur
from .enemi import enemi
from .projectil import projectil


class Monde: 

    def __init__(self,canvas):
        self.init_monde(canvas)


    def init_monde(self,canvas):
        j=joueur(canvas)
        j.creation_joueur(canvas)
        self.joueur=j
        
        e=enemi(canvas)
        e.creation_enemi(canvas)
        self.enemi=e

        p=projectil(canvas)
        p.creation_projectil(canvas)
        self.projectip=e
        