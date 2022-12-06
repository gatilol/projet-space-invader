from .joueur import joueur


class Monde: 

    def __init__(self,canvas):
        self.init_monde(canvas)


    def init_monde(self,canvas):
        j=joueur(canvas)
        j.creation_joueur(canvas)
        self.joueur=j
        
        